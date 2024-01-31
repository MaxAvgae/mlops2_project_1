#!/usr/bin/python3

import pandas as pd


url_train = 'https://raw.githubusercontent.com/MaxAvgae/mlops_data/main/train.csv'
url_test = 'https://raw.githubusercontent.com/MaxAvgae/mlops_data/main/test.csv'
train_df = pd.read_csv(url_train)
test_df = pd.read_csv(url_test)


train_df.to_csv('~/mlops2_project_1/data/raw/train.csv', sep=',', index = False)
test_df.to_csv('~/mlops2_project_1/data/raw/test.csv', sep=',', index = False)
