library(ggplot2)
library(readr)
library(dplyr)
library(tidyr)

# Load the data (please adapt to your own path)
data <- read_csv("/Users/gerardfont/Documents/Gerard/Master_BiomedicalDataScience/00_Master_THESIS/code/pyMSpro/data/processed/2022_Huffman/limmaCorrected_normed_prePCA_Priori_mrri02_PIF50_DART_1pFDR.csv")

# The file contains header
data <- data[,-1]


# Perform PCA and use the Group column as the color
pca <- prcomp(t(data), scale = TRUE)

# Plot the variance
plot(pca, type = "l")


# Calculate the cumulative variance explained
variance_explained <- cumsum(pca$sdev^2) / sum(pca$sdev^2)
cumulative_variance <- data.frame(PC = seq_along(variance_explained), Variance = variance_explained)

# Create a plot for cumulative variance explained in blue color
variance_plot <- ggplot(cumulative_variance, aes(x = PC, y = Variance)) +
  geom_line(color = "blue") +
  geom_point(color = "blue") +
  theme_minimal() +
  ggtitle("Cumulative Variance Explained") +
  theme(legend.position = "bottom")

# add the 90% line and the 95% line
variance_plot <- variance_plot +
  geom_hline(yintercept = 0.9, linetype = "dashed", color = "pink") +
  geom_hline(yintercept = 0.95, linetype = "dashed", color = "red")

# add the vertical line corresponding to the number of PCs that explain 95% of the variance and 90%
variance_plot <- variance_plot +
  geom_vline(xintercept = which(cumulative_variance$Variance >= 0.95)[1], linetype = "dashed", color = "#444444") +
  geom_vline(xintercept = which(cumulative_variance$Variance >= 0.9)[1], linetype = "dashed", color = "#dddddd")

# Display the plots
print(variance_plot)



