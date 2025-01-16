# Functional Enrichment analysis with ORA and FCS methods (using ClusterProfile)

# Load the necessary libraries
library(clusterProfiler)
library(enrichplot)
if (!requireNamespace("ReactomePA", quietly = TRUE)) { 
  install.packages("ReactomePA") 
} 
library(ReactomePA) 
if (!requireNamespace("org.Mm.eg.db", quietly = TRUE)) { 
  install.packages("org.Mm.eg.db") 
} 
library(org.Mm.eg.db)


# Load the DEG data (please adapt to your own path)
deM0 <- read.csv("/Users/gerardfont/Documents/Gerard/Master_BiomedicalDataScience/00_Master_THESIS/code/pyMSpro/results/DEG_M0.csv", sep="\t", header=TRUE)

# Load the ranked list data (please adapt to your own path)
rankM0 <- read.csv("/Users/gerardfont/Documents/Gerard/Master_BiomedicalDataScience/00_Master_THESIS/code/pyMSpro/results/Rank_M0_M1.csv", sep="\t", header=TRUE)

# Use the en
mart_mouse <- useMart("ensembl", dataset = "mmusculus_gene_ensembl")

# -- ORA -----------------------------------------------------------------------------------------------------------------------

# Retrieve the gene symbols from deM0$Gene
gene_symbols <- deM0$Gene

# Get Entrez IDs for the given gene symbols from mouse dataset
entrez_ids_mouse <- getBM(
  filters = "mgi_symbol",
  attributes = c("mgi_symbol", "entrezgene_id"),
  values = gene_symbols,
  mart = mart_mouse
)

# Transform to upper case the gene symbols of the entrez_ids_mouse data frame
entrez_ids_mouse$mgi_symbol <- toupper(entrez_ids_mouse$mgi_symbol)

# Merge the Entrez IDs with the original deM0 data frame
deM0 <- merge(deM0, entrez_ids_mouse, by.x = "Gene", by.y = "mgi_symbol", all.x = TRUE)

# check how many genes have not been matched
sum(is.na(deM0$entrezgene_id))

# remove them from the data frame
deM0 <- deM0[!is.na(deM0$entrezgene_id),]

# GO Enrichment (ORA)
ego <- enrichGO(gene          = deM0$entrezgene_id,
                OrgDb         = org.Mm.eg.db,
                ont           = "ALL",
                pAdjustMethod = "BH",
                pvalueCutoff  = 0.01,
                qvalueCutoff  = 0.05,
                readable      = TRUE)

dotplot(ego, showCategory=20) + theme(axis.text.y = element_text(size = 8))

# KEGG Enrichment (ORA)
eko <- enrichKEGG(gene          = deM0$entrezgene_id,
                  organism      = "mmu",
                  pvalueCutoff  = 0.05)

dotplot(eko, showCategory=20) + theme(axis.text.y = element_text(size = 8))

# Reactome enrichment (ORA)
ero <- enrichPathway(gene          = deM0$entrezgene_id,
                     organism      = "mouse",
                     pvalueCutoff  = 0.05)

dotplot(ero, showCategory=20) + theme(axis.text.y = element_text(size = 8))

# Number of enriched terms for KEGG
nrow(ero@result)


# -- FCS -----------------------------------------------------------------------------------------------------------------------

# Retrieve the gene symbols from rankM0$Gene
gene_symbols <- rankM0$Gene

# Get Entrez IDs for the given gene symbols from mouse dataset
entrez_ids_mouse <- getBM(
  filters = "mgi_symbol",
  attributes = c("mgi_symbol", "entrezgene_id"),
  values = gene_symbols,
  mart = mart_mouse
)

# Transform to upper case the gene symbols of the entrez_ids_mouse data frame
entrez_ids_mouse$mgi_symbol <- toupper(entrez_ids_mouse$mgi_symbol)

# Merge the Entrez IDs with the original rankM0 data frame
rankM0 <- merge(rankM0, entrez_ids_mouse, by.x = "Gene", by.y = "mgi_symbol", all.x = TRUE)

# check how many genes have not been matched
sum(is.na(rankM0$entrezgene_id))

# remove them from the data frame
rankM0 <- rankM0[!is.na(rankM0$entrezgene_id),]


gene_list <- setNames(rankM0$RANK, rankM0$entrezgene_id)
gene_list <- sort(gene_list, decreasing = TRUE)

# GO Enrichment (FCS)
gseaGO <- gseGO(geneList = gene_list, 
                 OrgDb = org.Mm.eg.db, 
                 ont = 'ALL', 
                 nPerm = 1000, 
                 minGSSize = 10, 
                 pvalueCutoff = 0.25,
                 verbose = FALSE) 

dotplot(gseaGO, showCategory=20) + theme(axis.text.y = element_text(size = 8))

# KEGG Enrichment (FCS)
gseaKEGG <- gseKEGG(geneList = gene_list, 
                    organism = 'mmu', 
                    nPerm = 1000, 
                    pvalueCutoff = 0.25,
                    verbose = FALSE)

dotplot(gseaKEGG, showCategory=20) + theme(axis.text.y = element_text(size = 8))

# Reactome Enrichment (FCS)
gsea_reactome <- gsePathway(geneList = gene_list, 
                            organism = "mouse", 
                            pvalueCutoff = 0.25 )

dotplot(gsea_reactome, showCategory=20) + theme(axis.text.y = element_text(size = 8)

