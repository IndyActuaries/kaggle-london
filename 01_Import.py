# <codecell>
import numpy as np
from pandas import DataFrame, Series
import pandas as pd

# <codecell>
#Run the following line once to define the data location on each machine
#%bookmark london E:/GitHub/kaggle-london/
%cd -b london
%pwd


# <codecell>
a=5
?a



# <codecell>
raw_train = pd.read_csv('Data_Raw/train.csv')
#?raw_train
raw_train
#?raw_train
#?raw_train.ix[0,0]
