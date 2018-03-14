import pandas as pd
import sys
import os

def file_is_empty(path):
    return os.stat(path).st_size==0

path = os.getcwd()
dirs = os.listdir(path)

df = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()

df = pd.read_csv('hsba.uk.txt', index_col = 0)
print pd.read_csv('hsba.uk.txt', index_col = 0)
#df = pd.read_csv('all.csv', index_col = 0)

for file in dirs:
    if file_is_empty(file)==False:
        if file.endswith('.txt'):
            print file
            df2 = pd.read_csv(file, index_col = 0)
            df2.rename(columns={'Close': file}, inplace=True)
            df3=df2[file]
            
            df=df.join(df3.to_frame(), how='outer')
            
            print file







#df = pd.merge(s1, df3[['Week', 'Colour', 'Val3']], how='left', on=['Week', 'Colour'])

#df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'}, inplace=True)

#df = pd.merge(s1, df3[['Week', 'Colour', 'Val3']], how='left', on=['Week', 'Colour'])

#df.to_csv(all.csv)

#df.loc['2017-12-05':'2017-12-12']