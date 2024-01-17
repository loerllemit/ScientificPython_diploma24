import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler
from matplotlib.cm import get_cmap
import matplotlib.patches as patches

def draw_cloud(center):
    
    radius = 0.005
    num_ellipses = 100
    alpha = 0.15

    for i in range(100):
        ellipse = patches.Ellipse(center, radius * (0.8 + i * 0.01), radius, color='white', alpha=alpha, zorder=100 - i)
        ax.add_patch(ellipse)
        radius += 0.001
        alpha -= 0.0015
        
cmap = plt.get_cmap('rainbow', 100)
fig, ax = plt.subplots(figsize=(8,5)) 
theta = np.linspace(0, np.pi, 100)
radius = 0.3  
al=0.0
for i in range (10):
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    plt.plot(x, y, color=cmap(0),alpha=al)
    radius-=0.0012
    al+=0.1
for i in range (100):
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    plt.plot(x, y, color=cmap(i))
    radius-=0.001
al=1
for i in range (10):
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    plt.plot(x, y, color=cmap(100),alpha=al)
    radius-=0.0012
    al-=0.1
    
draw_cloud((-0.2,0))
draw_cloud((-0.19,-0.01))
draw_cloud((-0.25,-0.005))
draw_cloud((-0.25,-0.01))
draw_cloud((-0.30,-0.01))
draw_cloud((-0.28,-0.03))
draw_cloud((-0.22,-0.03))

draw_cloud((0.2,0))
draw_cloud((0.19,-0.01))
draw_cloud((0.25,-0.005))
draw_cloud((0.25,-0.01))
draw_cloud((0.28,-0.03))
draw_cloud((0.22,-0.03))

draw_cloud((-0.1,0.3))
draw_cloud((-0.12,0.28))
draw_cloud((-0.06,0.29))

draw_cloud((-0.1+0.3,0.3-0.1))
draw_cloud((-0.12+0.3,0.28-0.1))
draw_cloud((-0.06+0.3,0.29-0.1))

ax.axhspan(-0.15,0.4, facecolor='lightskyblue', alpha=0.4)  # Blue for y >= 0
plt.ylim([-0.14,0.39])
plt.xlim([-0.4,0.4])

plt.savefig('rainbow.pdf')
plt.show()