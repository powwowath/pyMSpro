# pyMSpro

**Proteomics pipeline**
* Peptide Identification
* Protein inference
* Protein Quantification
* Data Normalization
* Imputation
* Batch correction
* Statistical Analysis *<----------------- Current focus*
* Enrichment Analysis
* Protein-Protein Interaction Analysis
* Pseudotime Analysis
* Visualization




### TODO
 * Taula comparativa (per estudi)
 * Use protein names from Uniprot
 * PCA per cell cycle phase / cell type
 * Plot amb el número de proteines que ens quedariem en funció del % de missing values que permetem
 * Functional enrichement analysis (STringDB) -> Fold change (average per celltype) vs. p-value




### CONSIDERATIONS
**Bioinformatic analysis**
Principal component analysis (PCA) and hierarchical clustering analysis were performed using the "gmodels" and "heatmap" package in R language, respectively. The Database for Annotation, Visualization, and Integrated Discovery (DAVID) V6.8 (https://david.‍ncifcrf.‍gov/home.‍jsp) was used to perform Gene Ontology (GO) with Kyoto Encyclopedia of Genes and Genomes (KEGG) pathway analyses by whole genome as background (Dennis et al., 2003). Reactome pathway analysis was performed using ClueGO plug-in and Cluepedia from Cytoscape (Bindea et al., 2009). Protein-protein interaction (PPI) network analysis was performed using Search Tool for the Retrieval of Interacting Genes/Proteins (STRING; https://string-db.‍org) (Szklarczyk et al., 2015), and interactions with a combined score of >0.15 were selected to construct the PPI networks using Cytoscape (Snel et al., 2000). The highly interactive modules were constructed with Molecular Complex Detection (MCODE) in Cytoscape (Bader and Hogue, 2003).





















<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
---

Main GIT commands:

  _**git add [file]**_  to add files to the staging area.

    example: git add .

  _**git commit**_  to create a new commit from changes added to the staging area.

    example: git commit -m "Added SQL Query to retrieve patients information"

  _**git branch [new_branch]**_  to create a new branch

    example: git branch notes_analysis

  _**git branch**_  to list existing local branches

    example: git branch notes_analysis

  _**git checkout [-b][branch_name]**_  to switch working directory to the specified branch (with -b: git will create the specified branch if it doesn't exist)

    example: git checkout -b microbiologic_analysis

  _**git pull [remote]**_  to fetch changes from the remote and merge current branch with its upstream

    example: git pull origin

  _**git push [--tags] [remote] [branch]**_ to push local branch to remote repository

    example: git push origin notes_analysis
