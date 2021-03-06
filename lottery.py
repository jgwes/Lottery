import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV, ElasticNetCV
from sklearn.metrics import mean_squared_error, make_scorer
from scipy.stats import skew
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns


pd.set_option('display.float_format', lambda x: '%.3f' % x)

raw = pd.read_csv("data/megamillionshistoryOD.csv")
print("raw : " + str(raw.shape))
