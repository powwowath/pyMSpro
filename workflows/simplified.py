import pandas as pd
from src.data.dea import differential_expression_analysis

# Load the data from the CSV file
prot_intensity = pd.read_csv('../data/processed/2021_Leduc/prot_proc.csv')
# Rename the first column to 'protein'
prot_intensity = prot_intensity.rename(columns={'Unnamed: 0': 'protein'})
# Convert the first column to the index of the DataFrame
prot_intensity = prot_intensity.set_index('protein')

# Load the data from the CSV file
metadata = pd.read_csv('../data/processed/2021_Leduc/anno.csv')
# Convert the first column of metadata to the index of the DataFrame
metadata = metadata.set_index('Unnamed: 0')
# Replace the column names with the values of the first row
metadata.columns = metadata.iloc[0]
# Drop the first row from the metadata DataFrame
metadata = metadata.drop(metadata.index[0])


# Concatenate the metadata to the protein intensity data frame
# TODO: We assume that both data frames have the same order for the columns
prot_intensity = pd.concat([metadata, prot_intensity], axis=0, ignore_index=False)
print(prot_intensity.head())





# Add a new row called "celltype" with Null values as the second row of the proc_intensity data frame
#new_row = pd.Series(name='celltype')
#prot_intensity = pd.concat([new_row, prot_intensity], ignore_index=True)
#print(prot_intensity.head())



# print(metadata[metadata["id"] == "i10"].values)
# # For each sample, fill in the celltype based on the metadata joining on the sample name (colname) and the row "id" in the metadata
# for sample in prot_intensity.columns:
#     print(sample)
#     prot_intensity.loc['celltype', sample] = metadata[metadata['id'] == sample]['celltype'].values[0]



# Insert in the second row the celltype of each sample
#prot_intensity.loc['celltype'] = metadata['celltype']


# Add a row to the protein intensity data frame with the celltype of each sample (from the metadata)
#prot_intensity.loc['celltype'] = metadata['celltype']
#print(prot_intensity.head())

#print(prot_intensity)

#

#dea = differential_expression_analysis(prot_intensity)
#dea.head()
