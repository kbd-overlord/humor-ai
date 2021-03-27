# Imports
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

from pylab import rcParams
import seaborn as sb

import scipy

import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import scale

# Settings
rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

# Jester dataset prep
path = r'data/jester-data-1.xls'

jokes = pd.read_excel(path)
