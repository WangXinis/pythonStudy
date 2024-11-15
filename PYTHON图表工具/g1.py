import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

'''Generating points to create a scatter plot'''
def scatter():
  x = np.random.random(100)
  y = x-np.random.random(100)
  z = np.random.randint(0,4,100)
  df = pd.DataFrame({'X':x, 'Y': y, 'Z':z})
  return df

'''Generating points to create a line plot'''
def line():
  x = np.arange(0,10,0.1)
  y_1 = np.sin(x)
  y_2 = np.sin(x+5)
  y_3 = np.sin(x+10)
  y_4 = np.sin(x+15)
  y_5 = np.sin(x+20)
  df = pd.DataFrame({'X':x,'y_1':y_1, 'y_2':y_2, 
                'y_3':y_3, 'y_4':y_4, 'y_5':y_5})
  return df

'''Sampling data from several distributions'''
def hist():
  x_1 = np.random.normal(1,0.1,1000)
  x_2 = np.random.gamma(1,0.25,1000)
  x_3 = np.random.normal(0.4, 0.1,1000)
  x_4 = np.random.normal(-0.1, 0.3,1000)
  df = pd.DataFrame({'X_1': x_1, 'X_2':x_2, 'X_3': x_3, 'X_4':x_4})
  return df
from aquarel import load_theme

theme = load_theme("arctic_light")
theme.apply()
# ... plotting code here
theme.apply_transforms()
with load_theme("arctic_light"):
  #plt.style.use('rose-pine')
  #plt.style.use('gruvbox')
  matplotlib.style.use("./gruvbox.mplstyle")
  fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(16,9))
  df = scatter()
  f= ax[0,0].scatter(df.X,df.Y, c=df.Z, s=50)
  ax[0,0].set_xlabel('X data')
  ax[0,0].set_ylabel('Y data')
  handles, labels = f.legend_elements(prop="colors", alpha=0.6)
  legend2 = ax[0,0].legend(handles, labels, loc="lower right")

  df=line()
  df.plot(x='X', ax=ax[0,1])

  df=hist()
  sns.kdeplot(df, fill=True, ax=ax[1,0])
  ax[1,0].set_xlabel('Value')

  sns.kdeplot(df, x="X_1", y="X_2", fill=True, ax=ax[1,1])
  sns.kdeplot(df, x="X_3", y="X_4",fill=True, ax=ax[1,1])
  ax[1,1].set_xlabel('Dist 1')
  ax[1,1].set_ylabel('Dist 2')

  plt.suptitle('Aquarel\narctic_light', fontsize=24)
  plt.savefig('arctic_light.jpg')
  plt.show()
if __name__ == '__main__':
    #t=hist()
    t=scatter()
    print(t)