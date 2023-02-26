# now that we created tables in create_tables.py, we have to insert data into them
#our data is stored in numerous files - some files like gene identity have only 1 row, while others have multiple rows
# we will first get all the relevant files for a table and create an array of them using the pd.read_csv command
#pd is instantiated from panda, which is a library of functions to deal with csvs
#panda has a built-in read_csv function which we are usiong below.
#glob is another library which gives us some functions to deal with multiple files and folders
import os
import glob
import pandas as pd
#-------------------------------------------------------------------

gene_csv = pd.read_csv('/Users/eshadesai/Desktop/MuteinFold_Project/MuteinFold/MuteinData/datasafe/datasets/esha.csv')
print("Number of files read for gene_csv - ", len(gene_csv))
#-------------------------------------------------------------------

path = '/Users/eshadesai/Desktop/MuteinFold_Project/MuteinFold/MuteinData/datasafe/genes/gene_pdbs'
csv_files = glob.glob(path + "/*.csv")
pdb_list = (pd.read_csv(filepath) for filepath in csv_files)
pdb_csv = pd.concat(pdb_list, ignore_index=True)
print("Number of files read for pdb_csv - ", len(pdb_csv))
#-------------------------------------------------------------------

path = '/Users/eshadesai/Desktop/MuteinFold_Project/MuteinFold/MuteinData/datasafe/genes/gene_id'
csv_idfiles = glob.glob(path + "/*.csv")
id_list = (pd.read_csv(filepath) for filepath in csv_idfiles)
id_csv = pd.concat(id_list, ignore_index=True)
print("Number of files read for id_csv - ", len(id_csv))
#-------------------------------------------------------------------
#get all the ddg files into an array - 2243 files
#we will read themn into the ddg_file_name table in populate_data.py

path = '/Users/eshadesai/Desktop/MuteinFold_Project/MuteinFold/MuteinData/datasafe/pdbs/mutation_data'
ddg_file_names_array = os.listdir(path)
#print ("temp : ",ddg_file_names_array)


"""
path = '/Users/eshadesai/Desktop/MuteinFold_Project/MuteinFold/MuteinData/datasafe/pdbs/mutation_data'
csv_mutfiles = glob.glob(path + "/*.csv")
mut_list = (pd.read_csv(filepath) for filepath in csv_mutfiles)
mut_csv = pd.concat(mut_list, ignore_index=True)
print("Number of files read for mut_csv - ", len(mut_csv))
#-------------------------------------------------------------------
"""