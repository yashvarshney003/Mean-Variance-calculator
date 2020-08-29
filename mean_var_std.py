import numpy as np
import copy

def calculate(nums:list):
  
  calculation = {}
  
  if(len(nums) == 9):
    array = np.array(nums).reshape(3,3)
    mean(array,calculation)
    variance(array,calculation)
    standard_deviation(array,calculation)
    max1(array,calculation)
    min1(array,calculation)
    sum1(array,calculation)
    
    
    print(calculation)
  else:
    raise ValueError("List must contain nine numbers.")
  return calculation


def mean(nums2,calculation):
  list1 = []
  num1 =  list(np.mean(nums2,axis=0))
  list1.append(num1)
  num1 =  list(np.mean(nums2,axis=1))
  list1.append(num1)
  num1 =  np.mean(nums2)
  list1.append(num1)

  #print(list1)
  calculation['mean'] = list1
  #print(calculation)
  

def variance(nums2,calculation):
  list1 = []
  num1 =  list(np.var(nums2,axis=0))
  list1.append(num1)
  num1 =  list(np.var(nums2,axis=1))
  list1.append(num1)
  num1 =  np.var(nums2)
  list1.append(num1)

  #print(list1)
  calculation['variance'] = list1
  #print(calculation)
def standard_deviation(nums2,calculation):
  list1 = []
  num1 =  list(np.std(nums2,axis=0))
  list1.append(num1)
  num1 =  list(np.std(nums2,axis=1))
  list1.append(num1)
  num1 =  np.std(nums2)
  list1.append(num1)

  #print(list1)
  calculation['standard deviation'] = list1
  #print(calculation)

def sum1(nums2,calculation):
  list1 = []
  num1 =  list(np.sum(nums2,axis=0))
  list1.append(num1)
  num1 =  list(np.sum(nums2,axis=1))
  list1.append(num1)
  num1 =  np.sum(nums2)
  list1.append(num1)

  #print(list1)
  calculation['sum'] = list1
  #print(calculation)


def max1(nums2,calculation):
  list1 = []
  num1 =  list(np.amax(nums2,axis=0))
  list1.append(num1)
  num1 =  list(np.amax(nums2,axis=1))
  list1.append(num1)
  num1 =  np.amax(nums2)
  list1.append(num1)

  #print(list1)
  calculation['max'] = list1
  #print(calculation)
def min1(nums2,calculation):
  list1 = []
  num1 =  list(np.amin(nums2,axis=0))
  list1.append(num1)
  num1 =  list(np.amin(nums2,axis=1))
  list1.append(num1)
  num1 =  np.amin(nums2)
  list1.append(num1)

  #print(list1)
  calculation['min'] = list1
  #print(calculation)
  

  
