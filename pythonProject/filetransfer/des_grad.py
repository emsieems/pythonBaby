import numpy as np
import matplotlib.pyplot as plt
import time

#first function
def load_data(fname):
    points = np.loadtxt(fname, delimiter=',')
    y_ = points[:,1]
    x_ = np.ones([len(y_),2])
    x_[:,0] = points[:,0]
    print('data here')
    return x_, y_

#second function
def evaluate_cost(x_,y_,params):
    tempcost = 0
    for i in range(len(y_)):
        tempcost += (y_[i] - (params[0] * x_[i,0]))
        return tempcost / float(100)

