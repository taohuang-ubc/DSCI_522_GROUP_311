The red wine quality prediction
================
DSCI 522 Group 311: Tao Huang, Hanying Zhang, Kirk Zhong
2020-01-24

# Summary

Using [UCI red wine quality
data](http://archive.ics.uci.edu/ml/datasets/Wine+Quality), based on a
dataset of 1599 examples, we are trying to build a model that can
predict the discrete wine garde by using the following red wine’s
physiochemical properties:

1 - fixed acidity 2 - volatile acidity 3 - citric acid 4 - residual
sugar 5 - chlorides 6 - free sulfur dioxide 7 - total sulfur dioxide 8 -
density 9 - pH 10 - sulphates 11 - alcohol

We are trying to answer the following research question:

1.  Can we build a machine learning model that can predict the red wine
    quality based on its physiochemical properties
2.  What properties are the most important features that influence the
    quality of red wine

Our machine learning model is able to predict the class of red wine with
relatively low mean squared error of 0.38 and more importantly, we are
able to discover the features that the really impact the quality of the
red wine.

# Analysis

The Analysis portion of this project is done by Python. A standard
scaler is used to scale all features into the same scale. To perform
feature selection, we use scikit-learn’s linear regression as an
estimator and perform recursive feature selection. Reragding the number
of features to select, we try the number from 1 to 11 (sum of features),
we found after selecting six features, if we selected more, the model
stop improving. Then we perform linear regression on the top six
features by using scikit-learn’s linear regression model.

The following Python packages were used in this project:

## R

  - docopt (de Jonge 2018)

  - knitr (Xie 2020)

  - tidyverse (Wickham 2017)

  - janitor(Firke 2019)

  - reshape2(Wickham 2007)

  - caret(Kuhn 2020)

## Python

  - docoptpython (Keleshev 2014)

  - request(Reiz 2019)

  - pandas(Safia Abdalla 2019)

  - numpy(Walt, Colbert, and Varoquaux 2011)

  - altair(VanderPlas et al. 2018)

  - scikit-learn(Buitinck et al. 2013)

# Results

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
