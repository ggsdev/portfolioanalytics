
import pandas as pd
import sys
import os


#df = pd.read_csv('all.csv', index_col = 0)
df2 = df.loc['2012-01-03':'2013-01-01']
series=df.loc['2012-01-03']
series=series[series<5]
series=series[series>0]
df3=df2[series.index]
df3len=len(df3.columns)
df4=df3/df3.iloc[0]-1
df3len=len(df3.columns)
df4['sum']=df4.sum(axis=1)
df4['prc']=df4['sum']/df3len