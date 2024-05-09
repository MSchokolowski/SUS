#!/usr/bin/env python3 
import matplotlib.pyplot as plt 
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

import math, os 
import numpy as np
from pylab import meshgrid,cm
from params import Parameters


def ackley(x):
  n = len(x)
  a = 20
  b = 0.2
  c = 2 * math.pi

  fx = -a * math.exp(-b * math.sqrt(1 / n * sum(i**2 for i in x))) - math.exp(1 / n * sum(math.cos(c * i) for i in x)) + a + math.exp(1)

  return(fx)


def test_wrapper(r, step_size):
  x = np.arange(-r, r+step_size, step_size)
  y = np.arange(-r, r+step_size, step_size)
  X,Y = meshgrid(x,y)
  Z = np.zeros((int(r*2 / step_size) + 1, int(r*2 / step_size) + 1))
  for idx_i, i in enumerate(x):
    for idx_j, j in enumerate(y):
      x_ij = [i,j]
      Z[idx_i,idx_j] = ackley(x_ij)
  return(X,Y,Z)


def plot_ackley(X,Y,Z):
  fig = plt.figure()
  ax = fig.add_subplot(projection='3d')
  surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, 
                      cmap=cm.RdBu,linewidth=0, antialiased=False)

  ax.zaxis.set_major_locator(LinearLocator(10))
  ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

  fig.colorbar(surf, shrink=0.5, aspect=5)

  plt.show()
      



if __name__ == '__main__':
  X,Y,Z = test_wrapper(4, 0.1)
  plot_ackley(X,Y,Z)

  #params = Parameters('params')
  #print(params.x_ini)

