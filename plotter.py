# Importing libraries
import pandas as pd    
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#plotter has two functions plot_hist() and plot_avg()

def plot_hist(val,n):
    print ("n - ", n)
    if n == "6":
        #print ("val = ", val)
        data = np.array(val)
        print ("Data received for plotting = ",data)
        b = 500
        print("********note bins is hardcoded to ",b, "********")
        print ("max value of ddg list: ", np.max(data))
        print ("min value of ddg list: ", np.min(data))
        diff = (np.max(data) -  np.min(data))
        print ("diff between max and min: ", diff)
        print ("avg bin size  is diff/number of bins we defined : ", diff/b)
        
        # Create a histogram with 20 bins
        print ("create a hist with ", b, " bins")
        n, bins, patches = plt.hist(data, b,color='blue')
        
        print ("the number of items in each bin: ",n)
        print ("the edges of the bins: ",bins)
        print ("the patches are just the blocks: ",patches)
        #for i in range (0, len(data)):
        #    print (data[i])
        #print ("our list of ddg values is: ", data)

        #fancy stuff
        # Set the x-axis limits to include negative and positive DDG values
        plt.xlim([np.min(data),np.max(data)])
        # Add a vertical line at 0 to indicate the cutoff for stability
        plt.axvline(x=0, color='red', linestyle='--')
        # Add labels and a title to the plot
        plt.xlabel('DDG Value')
        plt.ylabel('Frequency')
        plt.title('Histogram of DDG Values')
    
    else:
        print("invalid choice")

    # Add a grid to the plot
    plt.grid(True)

    # Display the plot
    plt.show()

def plot_avg(ddg_list):
    #print("***Making plot for file", my_csv_file)
    #pdb_df = pd.read_csv(pop.populate_ddg_info.ddg_csv)       #read the csv file
    pdb_df = pd.DataFrame(ddg_list, columns=['source', 'pdb', 'score', 'pdb_mutation', 'pdb_residual', 'pdb_chain', 'gene_number', 'mut_from', 'mut_to', 'ddg'])       #create panda dataframe from the sql read earlier
    print("***length: ", len(pdb_df))
    print ("***data: ", pdb_df)

    #pdb_df["pdb_residual"] = pd.to_numeric(pdb_df["pdb_residual"])                #pdb_residual is the column under which the gene number is stored; the actual gene_no column in csv is blank!!!!!!!!!!!
    pdb_df = pdb_df.groupby(["pdb_residual","mut_from"])["ddg"].mean()       #mean of ddg for every group of gene number and mut_from values
    pdb_df = pdb_df.reset_index()                                       #somethign to do with resetting index???
    pdb_df.columns = ["pdb_residual","mut_from","ddg"]                       #get the columns you need to print
    print("test x ",pdb_df)
    print("There are", len(pdb_df["pdb_residual"]),"rows")
    print("The max gene_no is", max(pdb_df["pdb_residual"]))
    

    ttl = "MuteinFold simple plot of a single pdb ddg, Number of rows - " + str (len(pdb_df))
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    fig.suptitle(ttl)    
    colors = {'D':'tab:blue', 'E':'tab:orange', 'F':'tab:green', 'G':'tab:red', 'H':'tab:purple', 'I':'tab:brown', 'J':'tab:pink'}
    sns.scatterplot(x='pdb_residual', y='ddg', data=pdb_df, hue='mut_from')
    plt.grid(True)
    plt.show()