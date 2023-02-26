import os
import dbapi
import api_implementation
import plotter as plt

option = 0

os.system('cls')      #Clear the screen

print("#### WELCOME TO THE GENE DATABASE - WHAT WOULD YOU LIKE TO DO ####")
print(" Choose one of the below options")
print ("Type 1 - To find the length of a gene")
print ("Type 2 - To find the maps for a gene")
print ("Type 3 - To find the number of mutants for a gene")
print ("Type 4 - To find the pdb data for a given gene-mutant combination")
print ("Type 5 - To find the ddg value for a specific gene mutant")
print ("Type 6 - To plot a histogram of ddg values given gene name")
print ("Type 7 - To find all the ddg values for a given gene")

choice = input("Please enter your choice : ")


if choice == "1":

    print("---- gene length ----")
    gene_name = input("Please enter the gene name : ")
    print(gene_name)
    value = dbapi.gene_length(gene_name)
    print("The length of ", gene_name , " is ", value)

elif choice == "2":

    print("---- number of gene maps from the pdb file ----")
    gene_name = input("Please enter the gene name : ")
    print(gene_name)
    map_names = dbapi.gene_maps(gene_name)
    print("The maps for gene ", gene_name , " are ", map_names)

elif choice == "3":

    print("---- number of mutants for a given gene name ----")
    gene_name = input("Please enter the gene name : ")
    print(gene_name)
    value = dbapi.gene_mutants(gene_name)
    print("The number of mutants for gene ", gene_name , " are ", value)

elif choice == "4":

    print("---- pdb info for a given gene name and pdb_mutant----")
    gene_name = input("Please enter the gene name : ")
    print(gene_name)
    pdb_mutant = input("Please enter the pdb_mutant for this gene : ")
    print(pdb_mutant)
    values = dbapi.mutant_ddg_info(gene_name, pdb_mutant,choice)
    print ("The pdb information for gene ", gene_name , " : ", pdb_mutant, " = ", values)

elif choice == "5":
    print("---- ddg info for a specific gene mutant")
    gene_name = input("Please enter the gene name : ")
    print(gene_name)
    pdb_mutant = input("Please enter the pdb_mutant for this gene : ")
    print(pdb_mutant)
    ddg_value = dbapi.mutant_ddg_info(gene_name, pdb_mutant, choice)
    print ("The ddg value for gene ", gene_name , " : ", pdb_mutant, " = ", ddg_value)

elif choice == "6":
    print("---- ddg values for a given gene and gene number")
    gene_name = input("Please enter the gene name : ")
    print(gene_name)
    #gene_number = input("Please enter the gene number for this gene : ")
    #print(gene_number)
    ddg_value = dbapi.mutant_ddg_info(gene_name, 0, choice)
    
    #for row in ddg_value:
    #    print ("value ", row)

    #print ("The ddg values for gene ", gene_name , " : " , ddg_value)
    plt.plot_hist(ddg_value, choice)

elif choice == "7":
    print("---- average of all mutations for a given gene")
    gene_name = input("Please enter the gene name : ")
    print(gene_name)
    ddg_value = dbapi.mutant_ddg_info(gene_name, 0, choice)     #here you get the complete combined list of all pdbs for that gene
    
    plt.plot_avg(ddg_value)         #call the avg plot function in plotter


else:
    print("invalid choice")