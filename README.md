# pyMSpro

**Proteomics pipeline**
* Peptide Identification
* Protein inference
* Protein Quantification
* Data Normalization
* Imputation
* Batch correction
* Statistical Analysis <----------------- Current focus
* Enrichment Analysis
* Protein-Protein Interaction Analysis
* Pseudotime Analysis
* Visualization





 - Taula comparativa (per estudi)
 - Use protein names from Uniprot
 + PCA per cell cycle phase / cell type
 + Plot amb el número de proteines que ens quedariem en funció del % de missing values que permetem
 - Functional enrichement analysis (STringDB) -> Fold change (average per celltype) vs. p-value


























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
