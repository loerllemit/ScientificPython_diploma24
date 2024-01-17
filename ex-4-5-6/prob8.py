#%%
import numpy as np

class MyMatrix:
    def __init__(self,N) :
        self.N = N
        self.matrix = np.random.random((self.N,self.N))
    
    def inverse(self):
        return np.linalg.inv(self.matrix)
    
    def determinant(self):
        return np.linalg.det(self.matrix)
    
    def eigenvalues(self):
        return np.linalg.eigvals(self.matrix)
    
    def __add__(self,other):
        return self.matrix + other.matrix
    
    def __mul__(self,other):
        return np.matmul(self.matrix,other.matrix)

#%%
N=4
matrix1=MyMatrix(N)
matrix2=MyMatrix(N)
print('matrix 1:',matrix1.matrix)
print('matrix 2:',matrix2.matrix)
print('matrix 1 inverse:',matrix1.inverse())
print('matrix 1 determinant:',matrix1.determinant())
print('matrix 1 eigenvalues:',matrix1.eigenvalues())
print('matrix add:',matrix1+matrix2)
print('matrix multiply:',matrix1*matrix2)

# %%
