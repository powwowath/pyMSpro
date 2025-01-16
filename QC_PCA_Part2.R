# Load necessary libraries
library(ggplot2)
library(data.table)

# Load the data (please adapt to your own path)
file_path <- "/Users/gerardfont/Documents/Gerard/Master_BiomedicalDataScience/00_Master_THESIS/code/pyMSpro/results/df_huffman_adata_var.csv"
data <- fread(file_path)

# Separate the features and the celltype column
features <- data[, 1:(ncol(data) - 1), with = FALSE]
celltype <- data[[ncol(data)]]

# Perform PCA
pca_result <- prcomp(features, scale. = TRUE)

# Create a data frame for visualization
pca_df <- data.frame(
  PC1 = pca_result$x[, 1],
  PC2 = pca_result$x[, 2],
  CellType = as.factor(celltype)
)

# Plot the PCA result
ggplot(pca_df, aes(x = PC1, y = PC2, color = CellType)) +
  geom_point(size = 2, alpha = 0.7) +
  labs(
    title = "PCA of Gene Intensities",
    x = "Principal Component 1",
    y = "Principal Component 2"
  ) +
  theme_minimal() +
  scale_color_brewer(palette = "Set1")


# Calculate the cumulative variance explained
variance_explained <- cumsum(pca_result$sdev^2) / sum(pca_result$sdev^2)
cumulative_variance <- data.frame(
  PC = seq_along(variance_explained),
  Variance = variance_explained
)

# Print the cumulative variance explained values * 100
print(variance_explained * 100)

# Plot the variance explained
pca_plot <- ggplot(cumulative_variance, aes(x = PC, y = Variance)) +
  geom_line(color = "blue") +
  geom_point(color = "blue") +
  labs(
    title = "Cumulative Variance Explained",
    x = "Principal Component",
    y = "Variance Explained"
  ) +
  theme_minimal() +
  geom_hline(yintercept = 0.9, linetype = "dashed", color = "pink") +
  geom_hline(yintercept = 0.95, linetype = "dashed", color = "red")

pca_plot







