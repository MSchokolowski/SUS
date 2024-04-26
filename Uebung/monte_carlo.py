#!/usr/bin/env python3 
import sys, os, argparse, random, math
import string

from params import Parameters
from ackley import ackley




def parse_arguments():
  p = argparse.ArgumentParser(description='monte-carlo')
  p.add_argument('params')
  return p.parse_args()

def get_trial_x(x_ini, x_delta):
  idim = random.randint(0, len(x_ini)-1)
  x_trial = x_ini
  step = x_delta * (2 * random.uniform(0.0, 1.0) - 1)
  x_trial[idim] = x_trial[idim] + step

def monte_carlo(n_step, x_ini, x_delta, e, temp):
  for i in range(n_step):
    print('tut')
    x_trial = get_trial_x(x_ini, x_delta)
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
      print(e_trial)
      print(x_trial)
      e = e_trial
      x = x_trial

if __name__ == '__main__':
  args = parse_arguments()
  params = Parameters(args.params)

  random.seed = params.seed
  e_ini = ackley(params.x_ini)
  monte_carlo(params.n_step, params.x_ini, params.x_delta, e_ini, params.ini_temp)

