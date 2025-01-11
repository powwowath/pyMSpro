# Install and load the biomaRt package
if (!requireNamespace("biomaRt", quietly = TRUE)) {
  install.packages("biomaRt")
}
library(biomaRt)
library(enrichplot)

# load /Users/gerardfont/Documents/Gerard/Master_BiomedicalDataScience/00_Master_THESIS/code/pyMSpro/results/DEG_M0.csv (separator is tab)
deM0 <- read.csv("/Users/gerardfont/Documents/Gerard/Master_BiomedicalDataScience/00_Master_THESIS/code/pyMSpro/results/DEG_M0.csv", sep="\t", header=TRUE)

# Use the ensembl datasets for Homo sapiens and Mus musculus
mart_human <- useMart("ensembl", dataset = "hsapiens_gene_ensembl")
mart_mouse <- useMart("ensembl", dataset = "mmusculus_gene_ensembl")

# Retrieve the gene symbols from deM0$Gene
gene_symbols <- deM0$Gene

# Get Entrez IDs for the given gene symbols from human dataset
entrez_ids_human <- getBM(
  filters = "hgnc_symbol",
  attributes = c("hgnc_symbol", "entrezgene_id"),
  values = gene_symbols,
  mart = mart_human
)

# Get Entrez IDs for the given gene symbols from mouse dataset
entrez_ids_mouse <- getBM(
  filters = "mgi_symbol",
  attributes = c("mgi_symbol", "entrezgene_id"),
  values = gene_symbols,
  mart = mart_mouse
)

# Combine the results from both datasets
entrez_ids <- rbind(
  data.frame(Gene = entrez_ids_human$hgnc_symbol, EntrezID = entrez_ids_human$entrezgene_id),
  data.frame(Gene = entrez_ids_mouse$mgi_symbol, EntrezID = entrez_ids_mouse$entrezgene_id)
)

# Merge the Entrez IDs with the original deM0 data frame
deM0 <- merge(deM0, entrez_ids, by.x = "Gene", by.y = "Gene", all.x = TRUE)

# remove NA values
deM0 <- deM0[!is.na(deM0$EntrezID),]

# Get the enriched terms with ORA
#edo <- enrichDGN(deM0$EntrezID, organism="mmusculus")
edo <- enrichDGN(deM0$EntrezID)
barplot(edo, showCategory=20) 

# Get the enriched terms with GSEA
edo2 <- gseDO(geneList)
dotplot(edo, showCategory=30) + ggtitle("dotplot for FCS")


ridgeplot(edo2)

p1 <- gseaplot(edo2, geneSetID = 1, by = "runningScore", title = edo2$Description[1])
p2 <- gseaplot(edo2, geneSetID = 1, by = "preranked", title = edo2$Description[1])
p3 <- gseaplot(edo2, geneSetID = 1, title = edo2$Description[1])
cowplot::plot_grid(p1, p2, p3, ncol=1, labels=LETTERS[1:3])
dotplot(edo2, showCategory=30) + ggtitle("dotplot for GSEA")







