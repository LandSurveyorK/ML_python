'''
Created on 2017Äê2ÔÂ8ÈÕ

@author: WEI
'''
import matplotlib
import numpy 
from numpy import *
from matplotlib.finance import quotes_historical_yahoo
from datetime  import date
import pandas as pd


today = date.today()
today = date.today()
start = (today.year-1,today.month,today.day)
quotes = quotes_historical_yahoo('AXP',start,today)
df= pd.DataFrame(quotes)
print df

