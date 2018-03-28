from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-100,100,1000)
x = x.reshape((x.shape[0],1))
w = np.array([-1, 1, -1])
w = w.reshape((1, w.shape[0]))
b = np.array([-7, 4, 12])
b = b.reshape((1, b.shape[0]))
temp = np.matmul(x, w)+np.matmul(np.ones((x.shape[1],1)), b)
r = np.sum(temp, axis=1)

y = np.array([temp[i]/r[i] for i in range(x.shape[0])]).T
x = x.T
print x.shape
print y.shape
fig = plt.figure()
ax1 = fig.add_subplot(131)
ax1.plot(x[0],y[0])
ax2 = fig.add_subplot(132)
ax2.plot(x[0],y[1])
ax3 = fig.add_subplot(133)
ax3.plot(x[0],y[2])
plt.show()

