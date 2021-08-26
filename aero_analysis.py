''' Import Relevant Packages '''
import os, datetime
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline

def get_description(iteration_no=50):
    
    '''This function outputs a dictionary with the dataframes. Output will be a description of the dataframe's 
    statistical make up along the last few iterations,
    which is given as the input of thi function. The default value will be set to 50'''
    cwd = os.getcwd()
    #print(cwd)
    # ideas dor later. introduce control via os os lisdir ('.') to get current files in directory and manage pathing je nachdem was da gibt oder nicht
    #import os
        #if not os.path.exists(...):
                #os.makedirs(...)
    path_to_tables = '/Tables/'

    filenames = {'data1_excel': 'data1',
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
    'data_1500_csv':'SaveDataToCSV_DataToCSV_01500' } # this dict can definitely be automated instead of being hard coded

    print('Preparing pathnames')

    fullpaths = filenames.copy()

    for key in filenames:
        #print(key)
        if 'excel' in key.strip().lower():
            fullpaths[key] = cwd+path_to_tables+filenames[key]+'.xlsx'
        elif 'csv' in key.strip().lower():
            fullpaths[key] = cwd+path_to_tables+filenames[key]+'.csv'

    #print(fullpaths)


    print('Making Dataframes from excel files')
    dataframes = fullpaths.copy()
    for key in fullpaths:
        if 'v' in fullpaths[key][-1]:
            dataframes[key] = pd.read_csv(fullpaths[key]) #ergänze index col, other oarametrs
            #a= dataframes[key].head(10)
            #b = dataframes[key].describe()
            #print(a,b)
            print('.')
        elif 'x' in fullpaths[key][-1]:
            dataframes[key] = pd.read_excel(fullpaths[key])
            #a= dataframes[key].head(10)
            #b = dataframes[key].describe()
            #print(a,b)
            print('.')

    #print(dataframes)

    mod_df = dataframes.copy()
    datanames = [dataname for dataname, value in filenames.items()]



    # I should have dataframes for all tables her now

    # Now to output statistical value for last 50 iterations
    print('Making files in Output')
    #os.mkdir('cwd/Output') #or cwd and os.path.join fcn 
    for dataname in datanames:
        #catch errors with try except finally use pass and break sparingly
            my_frame = mod_df[dataname].iloc[-iteration_no:,:]
            my_cols = my_frame.columns
            statistic_desc = my_frame.describe()
            my_mean = my_frame.mean()
            try:
                output = statistic_desc.copy() #trying to add mean count etc. on leftmost col 
                output.insert(0, 'Quantities', ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'], True)
                output.to_csv(f'{cwd}/Output/{dataname}.csv', index=False)
                print(f'Made {dataname}.csv ...')
            except:
                pass
            finally:
                pass
            with open(f'{cwd}/Output/{dataname}.txt', 'w') as my_file:
                my_file.write(f'*-- Title: {dataname} --* \n\n')
                print(f'Made {dataname}.txt ...')
                my_file.write(f'==> Iterations seen are from the last {iteration_no} \n\n')
                my_file.write(f'==> Columns in Dataframe: \n{str(my_cols)}\n\n')
                my_file.write(f'==> Statistical Descriptions, see corresponding csv file:\n{str(statistic_desc)}\n\n')
                my_file.write(f'==> Mean along columns, probably:\n{str(my_mean)}\n\n')
                my_file.write('\n\n\n\n\n\n\n')
                pass
    
    print('Done!')
            #technically i could also output to csv instead of writing a txt file
    #can you get an f string o the lhs to declare varabiles *+?
    #worth da try
    #nope. obvs- its still n f string in the end
    #use .items() for better readability and shorter code. use dict comprehension to build dict with proper name
    #research hw to use os to get list of names for iterating through dict and assigning to dict anemes


if __name__ == '__main__':
    try:
        get_description()
    except ValueError as ve:
        print(ve)
        pass