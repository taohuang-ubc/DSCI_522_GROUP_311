# Docker file for DSCI_522_GROUP_311
# 
# January 2020

# Use continuumio/anaconda3 as base image
FROM continuumio/anaconda3 

# Install base R
RUN apt-get update && \
    apt-get install r-base r-base-dev -y && \
    apt-get install libcurl4-openssl-dev -y && \
    apt-get install libssl-dev -y

# install python packages   
RUN conda install requests 
RUN conda install numpy 
RUN conda install pandas 
RUN conda install altair -y 
RUN conda install pyjanitor -c conda-forge -y
RUN conda install scikit-learn

# Install R Packages
RUN Rscript -e "install.packages('testthat')" 
RUN Rscript -e "install.packages('docopt')"
RUN Rscript -e "install.packages('knitr')"
RUN Rscript -e "install.packages('tidyverse')"
RUN Rscript -e "install.packages('janitor')"
RUN Rscript -e "install.packages('reshape2')"
RUN Rscript -e "install.packages('virdis')"
RUN Rscript -e "install.packages('caret')"

# Put Anaconda Python in PATH
ENV PATH="/opt/conda/bin:${PATH}"

CMD ["/bin/bash"]

