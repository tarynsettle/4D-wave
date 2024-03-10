from math import pi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import FormatStrFormatter

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# The period is 2pi, with 6 equidistant points.
X = np.linspace(-2.0*pi, 2.0*pi, num=6)
Y = np.linspace(-2.0*pi, 2.0*pi, num=6)
Z = np.linspace(-2.0*pi, 2.0*pi, num=6)
X, Y, Z = np.meshgrid(X, Y, Z)

# Value T is a sine function of the sum of coordinates of the points.
T = np.sin(X + Y + Z)

# The fourth dimension is defined here as a colormap of value T.
# The colors are then projected onto the equidistant points.
wave = ax.scatter(X/pi, Y/pi, Z/pi, c=T, cmap=cm.hot,
                       linewidth=0, antialiased=False)

ax.set_title('Sinusoid plotted in four dimensions')

ax.xaxis.set_major_formatter(FormatStrFormatter('%g $\pi$'))
ax.set_xlabel('X')
ax.yaxis.set_major_formatter(FormatStrFormatter('%g $\pi$'))
ax.set_ylabel('Y')
ax.zaxis.set_major_formatter(FormatStrFormatter('%g $\pi$'))
ax.set_zlabel('Z')

fig.colorbar(wave, shrink=.4, aspect=7, label="sin(X + Y + Z)")

plt.show()