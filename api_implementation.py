"""
This is the implementation of the dbapi file, if anything changes it should be here
This can be replaced with another implementation in the dbapi
##############################
"""
# Sytem imports
import os
import sys
import sqlite3
import datetime
import glob
import pandas as pd
import config #This is my config file with things that could change like user names, passwords and locations
import populate_data as pop

my_db = config.db_location
conn = sqlite3.connect(my_db)
cur = conn.cursor()
#-----------------------------------------------------------------------------------
# What is the length of a given gene name?
def gene_length(gene_name):
    print("gene_length VALUE PASSED = ",gene_name)
    qry = "SELECT length FROM gene_identity WHERE name_of_gene = '" + gene_name +"' "
    print ("IMP2: ",qry)
    c = cur.execute(qry) 
    len = c.fetchone()
    print ("IMP2: ",len)
    return len
#-----------------------------------------------------------------------------------
# What are the maps against a given gene name?
def gene_maps(gene_name):
    sql = "select COUNT (*) from ddg_file_names WHERE file_name LIKE '%" + gene_name + "%'"
    c = cur.execute(sql)
    count = c.fetchall()
    print ("number of rows in ddg_file)_names - ", count)

    print("gene_maps VALUE PASSED = ",gene_name)
    print("search for this gene name in the ddg_file_names table and get the file name")

    qry = "SELECT * FROM ddg_file_names WHERE file_name LIKE '%" + gene_name + "%'"
    #qry = "SELECT * FROM ddg_file_names WHERE file_name LIKE '%ADAM29%'"
    print(qry)
    c = cur.execute(qry) 
    maps = c.fetchall()
    print ("gene_maps result: ",maps)
    return maps

  #-----------------------------------------------------------------------------------
# What are the number of mutatnts against a given gene name?
# I have the gene and pdb information  in gene_data_bank - Using the gene name I'll get the relevant pdb(s)
# Using the pdb(s) I'll query the ddg_file)_name table to read the correspoding csv files for those pdbs i.e. the xx_backgroun.csv files into the ddg_info table
# and then count the number of mutants

def gene_mutants(gene_name):
    print("in gene mutants: ", gene_name)
    pop.populate_ddg_info(gene_name)
    sql = "SELECT COUNT(*) from ddg_info"
    c = cur.execute(sql)
    count = c.fetchall()
    return count

def mutant_ddg_value(variable1, variable2, choice):
    print("in api: ", variable1, " ", variable2)
    #BEWARE variable1 in this case has to be gene_name for the populate function to work
    pop.populate_ddg_info(variable1) #this step reads all the information for a given gene name
    
    conn = sqlite3.connect(my_db)
    cur = conn.cursor()

    if choice == "4":
        sql = "SELECT * FROM ddg_info WHERE pdb_mutation = '" + variable2 + "'"
    elif choice == "5":
        sql = "SELECT ddg FROM ddg_info WHERE pdb_mutation = '" + variable2 + "'"
    elif choice =="6":
        #sql = " SELECT ddg FROM ddg_info WHERE pdb_residual = " + variable2 + ""
        #sql = " SELECT ddg FROM ddg_info WHERE pdb_residual = 1"
        sql = " SELECT ddg FROM ddg_info"
    elif choice =="7":
        sql = " SELECT * FROM ddg_info"          

    print (sql)
    c = cur.execute(sql) 
    ddg_values = c.fetchall()
    print ("checkpoint: ", c)

    return ddg_values