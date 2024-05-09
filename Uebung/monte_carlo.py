#!/usr/bin/env python3 
import argparse, random, math
import matplotlib.pyplot as plt
import numpy as np
import copy

from params import Parameters
from ackley import ackley




def parse_arguments():
  p = argparse.ArgumentParser(description='monte-carlo')
  p.add_argument('params')
  return p.parse_args()

def get_trial_x(x, x_delta):
  idim = np.random.randint(0, len(x))
  x_trial = copy.copy(x)
  step = x_delta * (2 * np.random.rand() - 1)
  x_trial[idim] = x_trial[idim] + step
  
  return(x_trial)

def monte_carlo(n_step, x, x_delta, e, temp):
  e_save = np.array([])
  x_save = np.array([])
  for i in range(n_step):
    e_save = np.append(e_save, e)
    x_save = np.append(x_save, x)
    x_trial = get_trial_x(x, x_delta)
    e_trial = ackley(x_trial)
    flag = False

    if (e_trial <= e):
      flag = True
    else:
      if (e_trial > e):
        deltaE = e - e_trial
        if (random.uniform(0.0, 1.0) < math.exp(deltaE / temp)):
          flag = True
    
    if (flag == True):
      print("energy:\t{}\tx:\t{}\n".format(e_trial, x_trial))
      e = copy.copy(e_trial)
      x = copy.copy(x_trial)
  
  return e_save, x_save
      
def plot_energy(e):
  x_values = list(range(1,len(e)+1))
  fig,ax = plt.subplots()
  
  ax.plot(x_values, e)
  ax.set_title('Plot of energies')
  ax.set_xlabel('step')
  ax.set_ylabel('energy-values')
  
  plt.show()
  
  
def plot_x(x):
  x_values = list(range(1,len(x)+1))
  fig,ax = plt.subplots()
  
  ax.plot(x_values, x[:,0])
  ax.plot(x_values, x[:,1])
  ax.plot(x_values, x[:,2])
  plt.ylim(-0.3,0.3)
  ax.set_title('Plot of x-values')
  ax.set_xlabel('step')
  ax.set_ylabel('x-values')
  
  plt.show()
  
def write_csv(filename, x):
  np.savetxt(filename, x, delimiter=',',fmt='%s')
  
  

if __name__ == '__main__':
  args = parse_arguments()
  params = Parameters(args.params)

  np.random.seed(params.seed)
  e_ini = ackley(params.x_ini)
  e_save, x_save = monte_carlo(params.n_step, params.x_ini, params.x_delta, e_ini, params.ini_temp)
  x_reshaped = np.reshape(x_save, (-1, 3))

  write_csv(params.foutname, x_reshaped)

  plot_energy(e_save)
  plot_x(x_reshaped)