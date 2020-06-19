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

    X_data = X_info[0]
    Y_data = Y_info[0]
    X_labels = X_info[1]
    Y_labels = Y_info[1]
    X_data = pd.DataFrame.from_records(X_data)
    Y_data = pd.DataFrame.from_records(Y_data)
    X_data.columns = X_data.iloc[0]
    Y_data.columns = Y_data.iloc[0]
    X_data = X_data.drop(X_data.index[0])
    Y_data = Y_data.drop(Y_data.index[0])

    X_data.set_index(X_data.columns[0], inplace = True)
    Y_data.set_index(Y_data.columns[0], inplace = True)
    X_ = X_data[X_labels]
    Y_ = Y_data[Y_labels]
    X = X_.apply(pd.to_numeric, errors = 'ignore')
    Y = Y_.apply(pd.to_numeric, errors = 'ignore')


    ixs = X.index.intersection(Y.index)

    if ixs.empty:
        raise Exception('No common X and Y subjects at ' +args["state"]["clientId"])
    else:
        X = X.loc[ixs]
        Y = Y.loc[ixs]
    Y = Y*1

    return (X, Y)
