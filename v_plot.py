'''Import local modules and plotting packages'''

import numpy as np
import pandas as pd
#%matplotlib inline

import matplotlib.pyplot as plt

import seaborn as sns
sns.set()

def plot_performance():
    ''' 
        Import local modules foremores. This function currently provides graphs with placeholder values.
        Dependencies include seaborn as sns, pyplot as plt, pandas ad pd and numpy as np'''


    from v_theo_max import v_max
    from v_curve_perf import v_curve

    import importlib

    #importlib.reload(v_theo_max)
    #importlib.reload(v_curve_perf)


    # Turning Speed Plot

    v_abs, v_rel, v_cont, R = v_curve(250, 0.8, 1, 5)
    #print(v_rel, v_abs, v_cont, R)

    data_curve = np.stack([R, v_rel, v_abs, v_cont], axis=1)
    #print(cols)

    df_curve = pd.DataFrame(data=data_curve, columns=['Cornering Radius','v_curve_rel', 'v_curve_abs', 'v_control_rel (C_l=0)'], dtype=float)
    #df_curve = pd.DataFrame(data={'Cornering Radius': R, 'v_curve_rel': v_rel, 'v_curve_abs': v_abs, 'v_0Cl_rel': v_cont}, columns=['Cornering Radius','v_curve_rel', 'v_curve_abs', 'v_control_rel (C_l=0)'], dtype=float)
    # This gives the last col NaNs for some reason
    print(df_curve.head(10))

    # plotting with matplotlib
    # ax = plt.gca()
    # df.plot(kind='line',x='Cornering Radius',y='v_curve_rel',ax=ax)
    # df.plot(kind='line',x='Cornering Radius',y='v_curve_abs', color='red', ax=ax)
    # plt.show()

    df_curve = df_curve.melt('Cornering Radius', var_name='v_curve', value_name='Performance')

    plot_curve=sns.lmplot(x='Cornering Radius', y='Performance' , hue='v_curve', data= df_curve)

    plt.ylim(-100, None)
    plt.xlim(0, None)

    plt.xticks(rotation=-45)
    plt.yticks(rotation=45)

    plt.xlabel('Cornering Radius in m')
    plt.ylabel('Relative Turning Performance')

    #plt.legend(bbox_to_anchor=(1, 1), loc=2)

    plt.title('Relative and Absolute Performance in Relation to Cornering Radius')

    plt.show()


    #Topspeed Plot

    v_ms, v_kmh, cd = v_max(250, A=12)
    #print(v_ms, v_kmh, cd)

    data_topspeed = np.stack([cd, v_ms,v_kmh], axis=1)
    df_topspeed = pd.DataFrame(data=data_topspeed, columns=['Drag Coefficient','v_max_ms', 'v_max_kmh'], dtype=float)
    #df_topspeed = pd.DataFrame({'Drag Coefficient': cd, 'v_max_ms': v_ms, 'v_max:kmh': v_kmh}, columns=['Drag Coefficient','v_max_ms', 'v_max_kmh'], dtype=float)
    print(df_topspeed.head(10))

    #print(df_topspeed.isnull().sum())
    #print(df_curve.isnull().sum())

    df_topspeed = df_topspeed.melt('Drag Coefficient', var_name='v_topspeed', value_name='v_max')

    plot_topspeed=sns.lmplot(x='Drag Coefficient', y='v_max' , hue='v_topspeed', data= df_topspeed)

    plt.ylim(-100, None)
    plt.xlim(0, None)

    plt.xticks(rotation=-45)
    plt.yticks(rotation=45)

    plt.xlabel('Drag Coefficient, C_d')
    plt.ylabel('Theoretical Topspeed, v in kmh')

    plt.title('Topspeed Function over C_d')

if __name__ == '__main__':
    plot_performance()
