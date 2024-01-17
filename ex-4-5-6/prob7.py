#%%
class complex():
    def __init__(self,real,imag) :
        self.real = real
        self.imag = imag
    
    def __add__(self,other):
        real=self.real+other.real
        imag=self.imag+other.imag
        return complex(real,imag)        

    def __sub__(self,other):
        real=self.real-other.real
        imag=self.imag-other.imag
        return complex(real,imag)  
    
    def __mul__(self,other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return complex(real,imag)  

    def __truediv__(self, other):
        a,b,c,d = self.real,self.imag,other.real,other.imag
        real = (a*c+b*d)/(c**2+d**2)
        imag = (b*c-a*d)/(c**2+d**2)
        return complex(real,imag)  

    def __str__(self):
        if self.imag <0:
            return f'{self.real} - {abs(self.imag)}I' 
        else:
            return f'{self.real} + {self.imag}I' 
# %%
ins1 = complex(1,2)
ins2 = complex(3,5)

print('add:',ins1 + ins2)
print('subtract:',ins1 - ins2)
print('multiply:',ins1 * ins2)
print('divide:',ins2 / ins1)