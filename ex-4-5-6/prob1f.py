import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Function to generate 3D torus coordinates
def generate_torus(R, r, theta, phi):
    x = (R + r * np.cos(phi)) * np.cos(theta)
    y = (R + r * np.cos(phi)) * np.sin(theta)
    z = r * np.sin(phi)
    return x, y, z

# Torus parameters
n_plot_points=25
R = 2  # Major radius
r = 1  # Minor radius
theta = np.linspace(0, 2 * np.pi, n_plot_points)
phi = np.linspace(0, 2 * np.pi, n_plot_points)
theta, phi = np.meshgrid(theta, phi)

fig = plt.figure(figsize=(16, 8))

# Style 1: Wireframe
ax = fig.add_subplot(131, projection='3d')
x, y, z = generate_torus(R, r, theta, phi)
ax.set_zlim(-3,3)
ax.view_init(36, 26)
ax.plot_wireframe(x,y,z, color="#0000FF")

ax.set_title('Wireframe')

# Style 2: Surface
ax = fig.add_subplot(132, projection='3d')
x, y, z = generate_torus(R, r, theta, phi)
ax.set_zlim(-3,3)
ax.view_init(37, 26)
my_col = cm.jet(np.random.rand(z.shape[0],z.shape[1]))
# available colormaps are here -  https://matplotlib.org/stable/tutorials/colors/colormaps.html
ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap='viridis')
ax.set_title('Surface')

# Style 3: used the same, but changed colormap
ax = fig.add_subplot(133, projection='3d')
x, y, z = generate_torus(R, r, theta, phi)
ax.set_zlim(-3,3)
ax.view_init(37, 26)
#example of how to contol colormaps with weird stuff
my_col = cm.jet(np.random.rand(z.shape[0],z.shape[1]))
ax.plot_surface(x,y,z,rstride=2,cstride=1,facecolors = my_col)
ax.set_title('Still surface, but weird')

plt.savefig('torus.pdf')
plt.show()
