The red wine quality prediction
================
DSCI 522 Group 311: Tao Huang, Hanying Zhang, Xugang Zhong
2020-01-24

## Summary

To answer the question about predicting the red wine quality based on
physiochemical properties, we propose a prediction model using linear
regression algorithm. Based on the 1599 samples with 11 original
physiochemical features, we deployed recursive feature elimination (RFE)
to select features by recursively considering smaller and smaller sets
of features. It turned out that 6 physiochemical properties is
significant contributing to a better model performance. Building such
model is valuable to support oenologist wine tasting evaluations and
improve wine production.

## Introduction

According to [British Columbia Wine
Institute](https://winebc.com/industry/media/quick-facts/), the BC wine
industry contributes approximately $2.8 billion annually to British
Columbia’s economy. To facilitate the development of BC wine industry,
stakeholders are seeking a better way to improve the wine production and
selling process with new techniques applied. Globally, wine
certification and quality assessment are essential given this context.

Wine quality assessment basically consists of two parts: the lab test
and the sensory test. Physicochemical lab tests generally characterize
wine based on features such as density, pH value, acidity, sugar, and
alcohol, etc. While the sensory test is mainly relying on qualified
experts. Due to the low interpretation of human sense, the relationship
between sensory tests and the lab tests is somehow compared to a black
box. The industry is curious about how ‘good’ the wine is, given the
physicochemical lab test results. Therefore, a model integrating
physiochemical lab tests and sensory tests is helpful in addressing the
industry concern, supporting the wine evaluation and thus improving
local wine production.

## Methodology

The data used in this project is obtain from the [University of
California Irvine Machine learning
Repository](http://archive.ics.uci.edu/ml/datasets/Wine+Quality). It
contains 1599 samples from red wine produced in Portugal. Each sample
represents 11 physiochemical properties (features) from lab tests and
also the sensory result (response) ranging from 0 to 10.

The Analysis portion of this project is done by Python. A standard
scaler is used to scale all features into the same scale. To perform
feature selection, we use scikit-learn’s linear regression as an
estimator and perform recursive feature selection. Reragding the number
of features to select, we try the number from 1 to 11 (sum of features),
we found after selecting six features, if we selected more, the model
stop improving. Then we perform linear regression on the top six
features by using scikit-learn’s linear regression model.

The following Python packages were used in this project:

### R

  - docopt (de Jonge 2018)

  - knitr (Xie 2020)

  - tidyverse (Wickham 2017)

  - janitor(Firke 2019)

  - reshape2(Wickham 2007)

  - caret(Kuhn 2020)

### Python

  - docoptpython (Keleshev 2014)

  - request(Reiz 2019)

  - pandas(Safia Abdalla 2019)

  - numpy(Walt, Colbert, and Varoquaux 2011)

  - altair(VanderPlas et al. 2018)

  - scikit-learn(Buitinck et al. 2013)

## Results

According to the optimization process, it turned out that 6 features are
the best combination for our model based on the training and testing
error.

<img src="../results/ranked_features.png" title="Figure 2. The relationship between MSE and number of featurs" alt="Figure 2. The relationship between MSE and number of featurs" width="100%" />

The six physiochemical properties and their weights are reported as
blow:

<img src="../results/feature_weight_plot.png" title="Figure 1. Feature weight" alt="Figure 1. Feature weight" width="90%" />

Based on the plot, we can see that: alchol is the most significant
feature followed by volatile acidity and
sulphates.

<img src="../results/prediction_result.png" title="Figure 3. Prediction results" alt="Figure 3. Prediction results" width="90%" />

## References

<div id="refs" class="references">

<div id="ref-sklearn">

Buitinck, Lars, Gilles Louppe, Mathieu Blondel, Fabian Pedregosa,
Andreas Mueller, Olivier Grisel, Vlad Niculae, et al. 2013. “API Design
for Machine Learning Software: Experiences from the Scikit-Learn
Project.” In *ECML Pkdd Workshop: Languages for Data Mining and Machine
Learning*, 108–22.

</div>

<div id="ref-docopt">

de Jonge, Edwin. 2018. *Docopt: Command-Line Interface Specification
Language*. <https://CRAN.R-project.org/package=docopt>.

</div>

<div id="ref-janitor">

Firke, Sam. 2019. *Janitor: Simple Tools for Examining and Cleaning
Dirty Data*. <https://CRAN.R-project.org/package=janitor>.

</div>

<div id="ref-docoptpython">

Keleshev, Vladimir. 2014. *Docopt: Command-Line Interface Description
Language*. <https://github.com/docopt/docopt>.

</div>

<div id="ref-caret">

Kuhn, Max. 2020. *Caret: Classification and Regression Training*.
<https://CRAN.R-project.org/package=caret>.

</div>

<div id="ref-request">

Reiz, Kenneth. 2019. *Request: Requests Allows You to Send Organic,
Grass-Fed Http/1.1 Requests, Without the Need for Manual Labor.*
<https://pypi.org/project/requests/#history>.

</div>

<div id="ref-pandas">

Safia Abdalla, Joris Van den Bossche, Tom Augspurger. 2019. *Pandas:
Powerful Python Data Analysis Toolkit*.
<https://github.com/pandas-dev/pandas>.

</div>

<div id="ref-altair">

VanderPlas, Jacob, Brian Granger, Jeffrey Heer, Dominik Moritz, Kanit
Wongsuphasawat, Arvind Satyanarayan, Eitan Lees, Ilia Timofeev, Ben
Welsh, and Scott Sievert. 2018. “Altair: Interactive Statistical
Visualizations for Python.” *Journal of Open Source Software*, December.
The Open Journal. <https://doi.org/10.21105/joss.01057>.

</div>

<div id="ref-numpy">

Walt, Stéfan van der, S Chris Colbert, and Gael Varoquaux. 2011. “The
Numpy Array: A Structure for Efficient Numerical Computation.”
*Computing in Science & Engineering* 13 (2). IEEE Computer Society:
22–30.

</div>

<div id="ref-reshape2">

Wickham, Hadley. 2007. “Reshaping Data with the reshape Package.”
*Journal of Statistical Software* 21 (12): 1–20.
<http://www.jstatsoft.org/v21/i12/>.

</div>

<div id="ref-tidyverse">

———. 2017. *Tidyverse: Easily Install and Load the ’Tidyverse’*.
<https://CRAN.R-project.org/package=tidyverse>.

</div>

<div id="ref-knitr">

Xie, Yihui. 2020. *Knitr: A General-Purpose Package for Dynamic Report
Generation in R*. <https://CRAN.R-project.org/package=knitr>.

</div>

</div>
