# <codecell>
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
#from pandas import DataFrame, Series
#import pandas as pd


# <codecell>
#Run the following line once to define the data location on each machine
#%bookmark london E:/GitHub/kaggle-london/
%bookmark -l
%cd -b london
%pwd


# <codecell>
feat_train = np.genfromtxt('Data_Raw/train.csv', delimiter=',')
feat_test = np.genfromtxt('Data_Raw/test.csv', delimiter=',')
resp_train = np.genfromtxt('Data_Raw/trainLabels.csv', delimiter=',')

# <codecell>
feat_train_means = np.mean(feat_train, 1)
#feat_train_means.
