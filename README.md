# Elmo

Welcome to Elmo! A one-stop gene mutation database.

###############################################################################################
Storage of files:

The database has three main folders: dataset, gene, pdb
dataset = contains the list of genes in the database
gene = contains infromation about the gene's identity and the pdb identifiers associated with that gene
pdb = contains all the mutation data for each gene and mutant

Make sure the gene/PDB data is saved in a PDB folder. 
- the identity data is stored in a folder called gene_id within the main 'gene' folder (genes/gene_id)
- the pdb identifier data is stored in a folder called gene_pdbs within the main 'gene' folder (database/pdb/gene_pdbs)

The mutation data is stored in a separate folder
- this contains all the mutation data for each gene and mutant in the 'pdb' folder (database/pdb/mutation_data)

###############################################################################################
Instructions to run the database:

- Once the repository is cloned, change the filepaths in read_csv.py and populate_data.py to the filepaths on your local computer. 

- Ensure the structure of the files stored locally are the same as shown. 

- Run each script once to store the data on the SQL dataframes. You will only need to do this once. 

- Finally, run testapi.py to interact with the database. 