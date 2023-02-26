#All our  detailed code implementation for querying the tables are in the api_implemention file
# here we instatiate or create an instance of that file called api_call so that we can invoke those code implementation from here by doing 
#api_call.<the function's name>

import api_implementation as api_call

#-------------------------------------------------------------------------------
# Q1: What is the length of a given gene; Input: gene name, Output: gene length?
#-------------------------------------------------------------------------------
def gene_length(gene_name):
    """Gets the length of a gene when you pass it a gene name
    Parameters
    ----------
    gene_name
    type: str         The name of the gene
    
    Returns
    ----------
    gene_length 
    type: int        the length of the gene
    """
    print("in dbapi ", gene_name)
    return api_call.gene_length(gene_name)
#-------------------------------------------------------------------------------
def gene_maps(gene_name):
    print("in dbapi ", gene_name)
    return api_call.gene_maps(gene_name)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def gene_mutants(gene_name):
    print("in dbapi ", gene_name)
    return api_call.gene_mutants(gene_name)
#-------------------------------------------------------------------------------
def mutant_ddg_info(variable1, variable2 ,choice):
    print("in dbapi ", variable1, "-", variable2, "-", choice)
    return api_call.mutant_ddg_value(variable1, variable2 ,choice)