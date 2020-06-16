 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:36:06 2020

@author: Fatemeh
"""
import os

import numpy as np
import pandas as pd


def csv_parser(args):
    """Read the csv files specified in inputspec.json and return the
    covariate matrix (X) as well the dependent matrix (Y) as dataframes"""
    input_list = args["input"]
    X_info = input_list["covariates"]
    Y_info = input_list["data"]

    X_file = open(os.path.join(args["state"]["baseDirectory"], X_info[0][0]))
    Y_file = open(os.path.join(args["state"]["baseDirectory"], Y_info[0][0]))

    X_ = pd.read_csv(X_file, header = 0)
    Y_ = pd.read_csv(Y_file, header = 0)
    X_.set_index(X_.columns[0], inplace = True)
    Y_.set_index(Y_.columns[0], inplace = True)
    X = X_.apply(pd.to_numeric, errors = 'ignore')
    Y = Y_.apply(pd.to_numeric, errors = 'ignore')

    #X_labels = X_info[1]
    #Y_labels = Y_info[1]
    ixs = X.index.intersection(Y.index)

    if ixs.empty:
        raise Exception('No common X and Y subjects at ' +args["state"]["clientId"])
    else:
        X = X.loc[ixs]
        Y = Y.loc[ixs]
    Y = Y*1

    return (X, Y)
