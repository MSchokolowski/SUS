#!/usr/bin/env python3
import matplotlib.pyplot as plt
import sys, re, math, argparse, tempfile, os, random
import numpy as np


def part_func(e, t):
  z = math.exp(-e/(8.3144621 * t))
  return z

def prob_z(e, t, z):
  p = part_func(e, t) / z
  return p

def mono(e, t):
  part_func_arr = []
  part_func_arr.append(part_func(e[0], t))
  part_func_arr.append(part_func(e[1], t))
  part_func_arr.append(part_func(e[2], t))
  
  z = sum(part_func_arr)
  
  prob_arr = []
  prob_arr.append(prob_z(e[0], t, z))
  prob_arr.append(prob_z(e[1], t, z))
  prob_arr.append(prob_z(e[2], t, z))
  
  
  s = -(prob_arr[0] * math.log(prob_arr[0]) + prob_arr[1] * math.log(prob_arr[1]) + prob_arr[2] * math.log(prob_arr[2]))
  
  for entry in range(len(part_func_arr)):
    print("{:.6e}\t{:.6e}\t{:.6e}".format(part_func_arr[entry], prob_arr[entry], prob_arr[entry] * math.log(prob_arr[entry])))
  print("{:.6e}\t{:.6e}".format(z, s))
  
def di(e, t, ww):
  z = 0
  e_saves = np.zeros((len(e), len(e)))  
  z_saves = np.zeros((len(e), len(e)))
  prob_saves = np.zeros((len(e), len(e)))
  if ww:
    for i in range(len(e)-1):
      for j in range(len(e)-1):
        e_ij = e[i] + e[j] - 5000 if (i == j) else e[i] + e[j]
        
        e_saves[i,j] = e_ij
        z_saves[i,j] = part_func(e_ij, t)
        z += z_saves[i,j]
  else:
    for i in range(len(e)):
      for j in range(len(e)):
        e_ij = e[i] + e[j]

        e_saves[i,j] = e_ij
        z_saves[i,j] = part_func(e_ij, t)
        z += z_saves[i,j]
          
  s = 0
  for i in range(len(e)):
    for j in range(len(e)):
      prob_ij = prob_z(e_saves[i,j], t, z)
      prob_saves[i,j] = prob_ij
      s += prob_ij* math.log(prob_ij)
      
  for i in range(len(e)):
    for j in range(len(e)):
      print("({},{}) & {} & {:.6e} & {:.6e} & {:.6e} \\".format(i+1, j+1, int(e_saves[i,j] / 1000), z_saves[i,j], prob_saves[i,j], prob_saves[i,j] * math.log(prob_saves[i,j])))
      
  print("&&{:.6e} & & {:.6e}".format(z, -s))
  

if __name__ == '__main__':
  e_1 = 0
  e_2 = -1000
  e_3 = -2000
  e = [e_1, e_2, e_3]
  t = 300000
  
  #mono(e, t)
  di(e,t, True)
  #di(e,t, False)
  
  
  
  
  
  