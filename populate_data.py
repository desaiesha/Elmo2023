##############################
# Sytem imports
import os
import sys
import sqlite3
import datetime #https://docs.python.org/3/library/datetime.html#examples-of-usage-datetime
# Project imports
import config #This is my config file with things that could change like user names, passwords and locations
import pandas as pd
import read_csv
##############################
my_db = config.db_location
last_gene_name = 0              #using this var to store the last gene_name queired so that you dont have to red csvs again if question is about same gene

#-------------UPDATE gene_name table------------------------------------------------------
conn = sqlite3.connect(my_db)
cur = conn.cursor()

#print ("clearing the gene_name table of any existing data")
sql = "delete from gene_name"
cur.execute(sql)    

for i,row in read_csv.gene_csv.iterrows():
    sql = "INSERT INTO gene_name (dataset, name_of_gene, dummy) VALUES (?,?,?)"
    cur.execute(sql, row)

#check the number of rows inserted and print the count
sql = "select COUNT (*) from gene_name"
c = cur.execute(sql)    
c1 = c.fetchone()
print ("gene_name table updated and has ", c1, " rows")

#commit the connection and close the cursor i.e. seal the deal
conn.commit()
cur.close()

#-------------UPDATE gene_data_bank table------------------------------------------------------
conn = sqlite3.connect(my_db)
cur = conn.cursor()

#print ("clearing the gene_data_bank table of any existing data")
sql = "delete from gene_data_bank"
cur.execute(sql)    

for i,row in read_csv.pdb_csv.iterrows():
    sql = "INSERT INTO gene_data_bank (organism, name_of_gene, pdb, url, exp_method, exp_detail, length, coverage, gene_map, dummy) VALUES (?,?,?,?,?,?,?,?,?,?) "
    cur.execute(sql, row)
    #print(row)

#check the number of rows inserted and print the count
sql = "select COUNT (*) from gene_data_bank"
c = cur.execute(sql)    
c1 = c.fetchone()
print ("gene_data_bank table updated and has ", c1, " rows")

#commit the connection and close the cursor i.e. seal the deal
conn.commit()
cur.close()

#-------------Update gene_indentity table------------------------------------------------------
conn = sqlite3.connect(my_db)
cur = conn.cursor()

#print ("clearing the gene_identity table of any existing data")
sql = "delete from gene_identity"
cur.execute(sql)    

print("updating gene_identity")
for i,row in read_csv.id_csv.iterrows():
    sql = "INSERT INTO gene_identity (organism, name_of_gene, accession, length, sequence, dummy) VALUES (?,?,?,?,?,?)"
    cur.execute(sql, row)
    #print(i, " > ", row)

#check the number of roqws inserted and print the count
sql = "select COUNT (*) from gene_identity"
c = cur.execute(sql)    
c1 = c.fetchone()
print ("gene_identity table updated and has ", c1, " rows")

#commit the connection and close the cursor i.e. seal the deal
conn.commit()
cur.close()

#-------------Update ddg_file_name table------------------------------------------------------
conn = sqlite3.connect(my_db)
cur = conn.cursor()

print ("clearing the ddg_file_names table of any existing data")
sql = "delete from ddg_file_names"
cur.execute(sql)    

print("updating ddg_file_names--************************************************************")
for row in read_csv.ddg_file_names_array:
    #print (row)
    sql = "INSERT INTO ddg_file_names (file_name) VALUES ('" + row + "')"
    cur.execute(sql)

conn.commit()
cur.close()

conn = sqlite3.connect(my_db)
cur = conn.cursor()

sql = "select COUNT(*) from ddg_file_names"
c = cur.execute(sql)
c1 = c.fetchall()

print ("number of rows in ddg_file)_names - ", c1)

#commit the connection and close the cursor i.e. seal the deal
conn.commit()
cur.close()


#-------------populate the ddg_info table with the requested xx_background.csv contents for a given gene name------------------------------------------------------
#this is defined as a function which can be called by whoever needs to refer the contents of the xx_background.csv files
def populate_ddg_info(gene_name):
    
    #step 1.5 - if you have already read the same gene name data in your last question, then you dont have to read the csvs again
    #you can skip and return back to the caller and tell them that you have already read the contents of the csvs for that gene name
    #to do this we have defined a gene_name in config which stores the last called gene_name.
    """
    global last_gene_name

    print("LAST GENE ", last_gene_name)
    if gene_name == last_gene_name:
        print ("exiting pop")
        return True
    else:
        last_gene_name = gene_name
        print ("last gene name update to: ", last_gene_name)
    """    
    conn = sqlite3.connect(my_db)
    cur = conn.cursor()

    #check the number of pdbs
    #sql = "select COUNT (*) from ddg_file_names WHERE file_name LIKE '%" + gene_name + "%'"
    #c = cur.execute(sql)
    #count = c.fetchall()
    #print ("number of rows in ddg_file_names - ", count)

    #print("gene_maps VALUE PASSED = ",gene_name)
    #print("search for this gene name in the ddg_file_names table and get the file name")
    
    #step 1 - get the file names relevant to the given gene name from the ddg_file_name table
    now = datetime.datetime.now()
    print ("step 1 getting all file names from ddg_file_names table: ", now.strftime("%Y-%m-%d %H:%M:%S"))
    
    qry = "SELECT * FROM ddg_file_names WHERE file_name LIKE '%" + gene_name + "%'"
    c = cur.execute(qry) 
    maps = c.fetchall()
    #print ("gene_maps result: ",maps)
    
    #step 2 - the file name in ddg_file_name also need their path so we can read the contents using pd.read_csv. so store the path in a str
    path = "/Users/eshadesai/Desktop/MuteinFold_Project/MuteinFold/MuteinData/datasafe/pdbs/mutation_data/"
    #create a empty array to store the path and the filename
    ddg_file_path_list = []
    
    #step 3 - iterate thru the query result earlier i.e. maps to go thru each file name and prefix the path to it and store the resulting complete path in dd_file_list
    for row in maps:
        str = row[0]
        print (path + str)
        ddg_file_path_list.append (path + str)
    print ("Number of csvs to read - ", len(maps))

    #print ("test : ",ddg_file_path_list)
    
    #step 4 - now start readin the contents of the csv files from ddg_file_list using panda's read_csv function
    now = datetime.datetime.now()
    print ("step 4.1 start to read csv : ", now.strftime("%Y-%m-%d %H:%M:%S"))    

    ddg_file_list = (pd.read_csv(filepath) for filepath in ddg_file_path_list)
    ddg_csv = pd.concat(ddg_file_list, ignore_index=True)           #remember this ddg_csv now holds all the content i.e. rows from the csvs we told it to read

    now = datetime.datetime.now()
    print ("step 4.2 read csv completed : " , now.strftime("%Y-%m-%d %H:%M:%S"))    

    #step 5 - having read all the contents ino the ddg_csv list, it's time to insert them into the table ddg_info
    #note we are now writing only the requested gene_name's csvs into the table comapred to what we orinigally did i.e. read all 25m CSV records which took an hour
    #start by emptying the table of any existign records
    now = datetime.datetime.now()
    print ("step 5.1 start clearing ddg_info : ", now.strftime("%Y-%m-%d %H:%M:%S"))    

    print ("clearing the ddg_info table of any existing data")
    sql = "delete from ddg_info"
    cur.execute(sql)  

    now = datetime.datetime.now()
    print ("step 5.2 ddg_info table cleared : ", now.strftime("%Y-%m-%d %H:%M:%S"))    


    #step 6 - now start inserting the new data
    now = datetime.datetime.now()
    print ("step 6.1 start writing csv into ddg_info table : ", now.strftime("%Y-%m-%d %H:%M:%S"))    

    for i,row in ddg_csv.iterrows():
        sql = "INSERT INTO ddg_info (source, pdb, score, pdb_mutation, pdb_residual, pdb_chain, gene_number, mut_from, mut_to, ddg) VALUES (?,?,?,?,?,?,?,?,?,?)"
        cur.execute(sql, row)
        #print(cur.lastrowid)
        #print("ddg_info inserted")

    now = datetime.datetime.now()
    print ("step 6.2 completed writing csv into ddg_info table : ", now.strftime("%Y-%m-%d %H:%M:%S"))    

    sql = "select COUNT (*) from ddg_info"
    c = cur.execute(sql)
    c1 = c.fetchall()
    print ("number of rows in ddg_info - ", c1)
    for row in c1:
        print ("value - ", row)
    print ("value 2 - ", c1)
    
    #commit the connection and close the cursor i.e. seal the deal
    conn.commit()
    cur.close()

    return True

