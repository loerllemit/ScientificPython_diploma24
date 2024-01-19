import numpy as np
import matplotlib.pyplot as plt

class gol():
    def __init__(self,filename,iter=1000):
        self.data=np.genfromtxt(filename).transpose()
        self.iter = iter

    def update(self):
        df = np.copy(self.data)
        for i in range(np.shape(self.data)[0]):
            for j in range(np.shape(self.data)[1]):
                    if i == np.shape(self.data)[0]-1:
                        i = -1
                    if j == np.shape(self.data)[1]-1:
                        j = -1
                        
                    z = [self.data[i,j+1],self.data[i,j-1],self.data[i-1,j],self.data[i+1,j],self.data[i+1,j+1],self.data[i+1,j-1],self.data[i-1,j-1],self.data[i-1,j+1]]
                    ones = z.count(1)

                    if self.data[i,j] == 1 and ones in [2,3]:
                        df[i,j] = 1
                    elif self.data[i,j] == 0 and ones == 3:
                        df[i,j] = 1
                    else:
                        df[i,j] = 0

        self.data = df 

    def display(self):
        for _ in range(self.iter):  
            self.update()  
            plt.pcolor(self.data, linewidths=2)        # , edgecolors='k' 
            plt.pause(0.1)
        plt.show()


# filename = "data/gun.txt"
filename = "data/ships.txt"


ins = gol(filename)
ins.display()
