import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2*np.pi,2*np.pi)
y = np.sin(x)*np.cos(x)
z = np.sin(x)*np.cos(x)
fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")
ax.plot(x,y,z)
ax.set_xlabel = "X"
ax.set_ylabel = "Y"
ax.set_zlabel = "Z"
plt.title("3D график")
plt.show()