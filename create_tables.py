#Sytem imports
import os
import sys
import config

# Get the sql library
import sqlite3
#create a variable to which we will assign our db i.e. the genes.db defined in the config file
my_db = config.db_location
#connect to that database using sqlite3.connect
conn = sqlite3.connect(my_db)

#to make it easy to execute all in one go, create a list or array of the sql commands to create tables
tables_to_create = []
tables_to_create.append("CREATE TABLE IF NOT EXISTS gene_name (dataset, name_of_gene, dummy, PRIMARY KEY (name_of_gene))")
tables_to_create.append("CREATE TABLE IF NOT EXISTS gene_data_bank (organism, name_of_gene, pdb, url, exp_method, exp_detail, length, coverage, gene_map, dummy)")
tables_to_create.append("CREATE TABLE IF NOT EXISTS gene_identity (organism, name_of_gene, accession, length, sequence, dummy)")
tables_to_create.append("CREATE TABLE IF NOT EXISTS ddg_file_names (file_name)")    #the files listed as xx_background.csv
tables_to_create.append("CREATE TABLE IF NOT EXISTS ddg_info (source, pdb, score, pdb_mutation, pdb_residual, pdb_chain, gene_number, mut_from, mut_to, ddg)")

#now to execute the query to create tables, you need to open a cursor. A cursor is a utility using which you can INVOKE methods or commands 
#to execute sqlite3 statements like insert data, fetch data, count number of rows etc.
with sqlite3.connect(my_db) as con:
    cur = con.cursor()
    for create_text in tables_to_create:
        print("Create text:",create_text)
        try:
            cur.execute(create_text)    
        except sqlite3.DatabaseError as err:
            print("Error:",err)            
    con.commit()
# The conn.commit basically seals the deal i.e. commits the executed sql statements i.e. ensures that they stay in there

############ after creation a check that we have what we intended  ############################
print("########### checking back what tables we have ###############")
with sqlite3.connect(my_db) as con:
    cur = con.cursor()                                
    for row in cur.execute("SELECT name FROM sqlite_master WHERE type='table'"):
        print(row)





