import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0,5,100)
y1 = np.sin(x)
y2 = np.cos(x + 0.2)
y3 = np.exp(x*x + 0.4)
y4 = np.sin(x*x + 0.6)
y5 = np.log(x + 0.8)
y6 = np.tan(x + 1)

# now we decide the actual figure size in inches
fig = plt.figure(figsize=(14,7))

plt.suptitle('Name of the whole picture',fontweight='bold', fontsize='x-large')
plt.subplots_adjust(hspace=0.3, top=0.8) 
# create subplots 231 means make a 2x3 grid and this is the first plot
plt.subplot(231)
#these are here to show that you can do the same here as for a single plot
plt.title('picture 1',fontsize = 'large',fontstyle='italic',fontweight='bold')
plt.ylabel('sin(x)',fontsize = 'xx-large',fontstyle='oblique',fontweight = 'heavy')
plt.xlabel('This is the $x$ axis',fontsize = 'xx-large',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y1,color='r')

plt.subplot(232)
plt.title('picture 2',fontsize = 'large',fontstyle='italic',fontweight='bold')
plt.ylabel('cos(x+0.2)',fontsize = 'xx-large',fontstyle='oblique',fontweight = 'heavy')
plt.xlabel('This is the $x$ axis',fontsize = 'xx-large',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y2,color='g')

plt.subplot(233)
plt.title('picture 3',fontsize = 'large',fontstyle='italic',fontweight='bold')
plt.ylabel('exp(x*x + 0.4)',fontsize = 'xx-large',fontstyle='oblique',fontweight = 'heavy')
plt.xlabel('This is the $x$ axis',fontsize = 'xx-large',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y3,color='b')

plt.subplot(234)
plt.title('picture 4',fontsize = 'large',fontstyle='italic',fontweight='bold')
plt.ylabel('sin(x*x + 0.6)',fontsize = 'xx-large',fontstyle='oblique',fontweight = 'heavy')
plt.xlabel('This is the $x$ axis',fontsize = 'xx-large',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y4,color='y')

plt.subplot(235)
plt.title('picture 5',fontsize = 'large',fontstyle='italic',fontweight='bold')
plt.ylabel('log(x + 0.8)',fontsize = 'xx-large',fontstyle='oblique',fontweight = 'heavy')
plt.xlabel('This is the $x$ axis',fontsize = 'xx-large',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y5,color='c')

plt.subplot(236)
plt.title('picture 6',fontsize = 'large',fontstyle='italic',fontweight='bold')
plt.ylabel('tan(x + 1)',fontsize = 'xx-large',fontstyle='oblique',fontweight = 'heavy')
plt.xlabel('This is the $x$ axis',fontsize = 'xx-large',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y6,color='m')
# removed extra white space
plt.tight_layout()
plt.savefig('function_family.pdf')
plt.show()