import pandas as pd
import numpy as np 
import pandas as pd 
import os
from plotly.offline import init_notebook_mode, iplot
import chart_studio.plotly as py
import plotly.figure_factory as FF
from plotly import tools
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import datetime
warnings.filterwarnings("ignore")
df = pd.read_csv('./MELBOURNE_HOUSE_PRICES_LESS.csv')
df1 = pd.read_csv('./Melbourne_housing_FULL.csv')
df = df.append(df1)
df.isnull().sum().sort_values(ascending=False)
no_missing_df = df[df['Price'].notnull()]
no_missing_df.isnull().sum().sort_values(ascending=False)
df = no_missing_df.copy()