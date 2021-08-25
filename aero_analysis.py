''' Import Relevant Packages '''
import os, datetime
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline

cwd = os.getcwd()
print(cwd)

path_to_tables = '/Tables/'

filenames = {'data1': 'data1',
'data2_excel':'data2',
'data3_excel': 'data3',
'data4_excel': 'data4',
'data_v1_desc_excel': 'DATA_v1_gerade_SeiteParabel_GurneyFlap_AbstandGross',
'data_v2_desc_excel': 'DATA_v2_gerade_SeiteGanz_GurneyFlap_AbstandGross',
'data_v3_desc_excel': 'DATA_v3_gerade_SeiteSchraeg_GurneyFlap_AbstandGross',
'data_v4_desc_excel': 'DATA_v4_gerade_SeiteSchraegCutUnten_GurneyFlap_AbstandGross',
'data_excel_original':'CSV_Example_original',
'data_excel_semik_original':'CSV_Example_Semikolon_original',
'data_excel_semik_aufg':'CSV_Example_Semikolon_aufgefuellt',
'data_1500_csv':'SaveDataToCSV_DataToCSV_01500' }

fullpaths = filenames.copy()

for key in filenames:
    print(key)
    if 'excel' in key.strip().lower():
        fullpaths[key] = cwd+path_to_tables+filenames[key]+'.xlsx'
    elif 'csv' in key.strip().lower():
        fullpaths[key] = cwd+path_to_tables+filenames[key]+'.csv'

print(fullpaths)

dataframes = fullpaths.copy()
for key in fullpaths:
    if 'v' in fullpaths[key][-1]:
        dataframes[key] = pd.read_csv(fullpaths[key]) #ergänze index col, other oarametrs
        a= dataframes[key].head(10)
        b = dataframes[key].describe()
        print(a,b)
    elif 'x' in fullpaths[key][-1]:
        dataframes[key] = pd.read_excel(fullpaths[key])
        a= dataframes[key].head(10)
        b = dataframes[key].describe()
        print(a,b)

print(dataframes)





# I should have dataframes for all tables her now

# Now to output statistical value for last 50 iterations

mod_df = dataframes.copy()

for key in dataframes:
    mod_df[key] = dataframes[key].iloc[-50::]
    print(mod_df[key], mod_df.describe())

#can you get an f string o the lhs to declare varabiles *+?
#worth da try
#nope. obvs- its still n f string in the end