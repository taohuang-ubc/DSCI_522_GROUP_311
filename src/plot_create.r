# author: Group 311 - Tao Huang, Xugang(Kirk) Zhong, Hanying Zhang
# date: 2020-01-24

"Creates plots for the training data and saves them as png files.
Usage: src/plot_create.r --x_train=<x_train> --y_train=<y_train> --output=<output>
  
Options:
--x_train=<x_train>     Path (including filename) to the feature set of the training data
--y_train=<y_train>     Path (including filename) to the target set of the training data
--output=<output>   Output file path of the generated plots
" -> doc

library(tidyverse)
library(docopt)
library(reshape2)

opt <- docopt(doc)

main <- function(x_train, y_train, output) {
    # read training data
    x <- read_csv(x_train)
    y <- read_csv(y_train)
    training_data <- cbind(x, y)

    # plot_1 - distribution of training set target
    plot_1 <- training_data %>% 
    ggplot(aes(quality)) + 
        geom_histogram(bins = 15)
    ggsave(paste0(output, "/quality_value_distribution.png"), plot_1, width = 8, height = 5)

    # plot_2 - distributions of all features
    plot_2 <- training_data %>% 
    gather(key = feature, value = value, -quality) %>% 
    mutate(feature = str_replace_all(feature, "_", " ")) %>% 
    ggplot(aes(x = value)) +
      facet_wrap(. ~ feature, scale = "free", ncol = 3) +
      geom_histogram(bins = 50)
    ggsave(paste0(output, "/feature_distributions.png"), plot_2, width = 20, height = 15)
    
    # plot_3 - correlation heatmap of the features
    corr <- cor(training_data)
    melted_corr <- melt(corr)
    plot_3 <- melted_corr %>% 
        ggplot(aes(x=Var1, y=Var2, fill=value)) + 
        geom_tile() +
        theme(axis.text = element_text(size = 12),
        axis.title.x = element_blank(),
        axis.title.y = element_blank())
    ggsave(paste0(output, "/feature_correlation_heatmap.png"), plot_3, width = 20, height = 15)
}

main(opt[["--x_train"]], opt[["--y_train"]], opt[["--output"]])