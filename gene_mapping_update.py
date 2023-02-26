"""
RSA: 25/01/2023
This adds the gene number into the file - mapping from the protein residue number

"""
### ENTER PARAMETERS HERE ###
gene_dir_path = '/Users/eshadesai/Desktop/MuteinFold_Project/MuteinFold/MuteinData/datasafe/genes/genes_new/'
pdb_dir_path = '/Users/eshadesai/Desktop/MuteinFold_Project/MuteinFold/MuteinData/datasafe/pdbs/mutation_data_updated/'
#######################################

import pandas as pd
from os import listdir
from os.path import isfile, join
from os.path import exists

##############################################################################################################################
### Functions needed for the mapping ###
##############################################################################################################################
def applyGeneMap(chain,residue,mapping):
    try:
        if "{" in mapping:
            segsa = mapping.split("{")
            segs = []
            for seg in segsa[1:]:
                segs.append(seg[:-1])        
            for seg in segs:
                g_p = seg.split(":")
                gg = g_p[0]
                pp = g_p[1]
                if len(g_p) > 2:
                    pp = g_p[2] # TOD bug for some reason the alphafold mapping has an extra :1: in the middle

                row_ch  = pp[0]
                if str(row_ch).upper() == str(chain).upper():
                    res_start = int(pp[1:].split("-")[0])
                    res_end = int(pp[1:].split("-")[1])
                    if int(residue) >= res_start and int(residue) <= res_end:
                        gene_start = int(gg.split("-")[0])
                        offset = res_start - gene_start
                        adj_gene = int(residue) - offset
                        return adj_gene
    except:
        pass
    return "-1"


def applyGeneMappingToAll():
    onlyfiles = [f for f in listdir(gene_dir_path) if isfile(join(gene_dir_path, f))]                
    for file in onlyfiles:                                   
        if "_pdbs" in file:                    
            nams = file.split("_")
            gene_name = nams[1]
            print("Ammending",file,"gene=",gene_name)              
            gene_df = pd.read_csv(gene_dir_path + file)                                  
            print(gene_df)
            pdbs = gene_df["pdb"]
            pdb_maps = gene_df["gene_map"]
            for i in range(0,len(pdbs)):
                pdb_file_name = gene_name.lower() + "_" + pdbs[i] + "_ddg_background.csv"
                if exists(pdb_dir_path + pdb_file_name):
                    gene_map = pdb_maps[i]            
                    gene_pdb_df = pd.read_csv(pdb_dir_path + pdb_file_name)                                                  
                    # augment the ddg with gene_no
                    gene_pdb_df["gene_no"] = gene_pdb_df.apply(lambda row: applyGeneMap(row["pdb_chain"],row["pdb_rid"],gene_map),axis=1)    
                    gene_pdb_df["gene_no"] = pd.to_numeric(gene_pdb_df["gene_no"])    
                    gene_pdb_df.to_csv(pdb_dir_path + pdb_file_name,index=False)
            
##############################################################################################################################
# Run the code
applyGeneMappingToAll()