#!/usr/bin/env python3 
import sys, os, argparse, random, math
import string
import matplotlib.pyplot as plt
import numpy as np
import csv

from params import Parameters
from ackley import ackley, plot_ackley




def parse_arguments():
  p = argparse.ArgumentParser(description='monte-carlo')
  p.add_argument('params')
  return p.parse_args()

def get_trial_x(x, x_delta):
  idim = random.randint(0, len(x)-1)
  x_trial = x
  step = x_delta * (2 * random.uniform(0.0, 1.0) - 1)
  x_trial[idim] = x_trial[idim] + step
  
  return(x_trial)

def monte_carlo(n_step, x, x_delta, e, temp):
  e_save = np.zeros(n_step)
  x_save = np.zeros((n_step, len(x)))
  for i in range(n_step):
    x_trial = get_trial_x(x, x_delta)
    e_trial = ackley(x_trial)
    e_save[i] = e_trial
    x_save[i] = x_trial
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
      e = e_trial
      x = x_trial
  
  return e_save, x_save
      
def plot_monte_carlo(e):
  x_values = list(range(1,len(e)+1))
  fig,ax = plt.subplots()
  
  ax.plot(x_values, e)
  ax.set_title('Plot of energies')
  ax.set_xlabel('step')
  ax.set_ylabel('energy')
  
  plt.show()
  
def write_csv(filename, x):
  with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    
    for row in x:
      writer.writerow(row)
  

if __name__ == '__main__':
  args = parse_arguments()
  params = Parameters(args.params)

  random.seed = params.seed
  e_ini = ackley(params.x_ini)
  e_save, x_save = monte_carlo(params.n_step, params.x_ini, params.x_delta, e_ini, params.ini_temp)

  plot_monte_carlo(e_save)
  write_csv(params.foutname, x_save)

  plot_ackley(x_save[:,0],x_save[:,1],x_save[:,2])