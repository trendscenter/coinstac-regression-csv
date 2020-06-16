# coinstac-regression-csv
Coinstac Code for Decentralized Regression (Normal Equation) for generic CSV files.
Input for each site contains two CSV files, the features and the labels (specified as X_file.csv and Y_file.csv).
The covariates do not need to be specified in inputspec file since they are read as part of CSV files.

Here UCI Boston housing dataset is used which can be found in the following link:\
https://archive.ics.uci.edu/ml/machine-learning-databases/housing/

Tools: Python 3.6.5, coinstac-simulator 4.2.0

Steps: \
1- sudo npm i -g coinstac-simulator@4.2.0 \
2- git clone https://github.com/trendscenter/coinstac-regression-csv.git \
3- cd coinstac-regression-csv \
4- docker build -t regression-general \
5- coinstac-simulator 
