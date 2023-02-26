import pandas as pd    
import matplotlib.pyplot as plt
import seaborn as sns

my_csv_file = '/Users/eshadesai/Desktop/MuteinFold_Project/MuteinFold/MuteinData/datasafe/pdbs/mutation_data/adam29_afq9ukf5-f1-model_v3_ddg_background.csv'

def make_plot_avg():
    print("Making plot for file", my_csv_file)
    pdb_df = pd.read_csv(my_csv_file)
    pdb_df["ddg"] = pd.to_numeric(pdb_df["ddg"])
    pdb_df["gene_no"] = pd.to_numeric(pdb_df["gene_no"])
    pdb_df = pdb_df.groupby(["gene_no","mut_from"])["ddg"].mean()
    pdb_df = pdb_df.reset_index()
    pdb_df.columns = ["gene_no","mut_from","ddg"]
    print(pdb_df)
    print("There are", len(pdb_df["gene_no"]),"rows")
    print("The max gene_no is", max(pdb_df["gene_no"]))
    ttl = "MuteinFold simple plot of a single pdb ddg"
    fig, ax = plt.subplots(1, 1, figsize=(11, 6))
    fig.suptitle(ttl)    
    colors = {'D':'tab:blue', 'E':'tab:orange', 'F':'tab:green', 'G':'tab:red', 'H':'tab:purple', 'I':'tab:brown', 'J':'tab:pink'}
    sns.scatterplot(x='gene_no', y='ddg', data=pdb_df, hue='mut_from')
    plt.show()

make_plot_avg()
