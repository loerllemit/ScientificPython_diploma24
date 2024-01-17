#%%
import numpy as np
from matplotlib import pyplot as plt

def plot_func(func):
    def wrapper(*args, **kwargs):
        x = np.linspace(0,100,1000)
        fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(5,6))
        ax.plot(x,func(x),color='blue',label='function')
        ax.set_title('Plot of f(x)',fontsize = 'large',fontweight='bold')
        ax.set_ylabel('f(x)',fontsize = 'medium',fontweight = 'heavy')
        ax.set_xlabel('x (arb.)',fontsize = 'medium',fontweight = 'heavy')
        ax.set_facecolor((1.0, 0.47, 0.42))
        ax.legend()
        plt.show()
    return wrapper


@plot_func
def my_f(x=0):
    return np.sin(x)

my_f(0)
# %%
