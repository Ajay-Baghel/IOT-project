import numpy as np
from sympy.stats import Levy
import math
import random
import matplotlib.pyplot as plt

class sensor:
    def __init__(self, type, x, y, x_e = 0, y_e = 0):
        self.type = type
        self.x = x
        self.y = y
        self.x_e = x_e
        self.y_e = y_e

# Optimization/cost function
def Fun(x,y, anchors, d):
    f = 0
    for i in range(3):
        # print(anchors[i].x,anchors[i].y )
        f +=  math.pow(math.sqrt(math.pow((x-anchors[i][0]),2) + math.pow((y-anchors[i][1]),2)) - d,2)
        # print(f)
    return f/3

def NMRA(x_lb,x_ub,y_lb,y_ub,maxIter,best,n,anchors):
    rats=[]
    workers=n-n//5
    breeders=n//5
    fitness=[]
    bp=0.5
    d = (x_ub-x_lb)/2
    for i in range(n):
        x1=x_lb+np.random.random()*(x_ub-x_lb)
        y1=y_lb+np.random.random()*(y_ub-y_lb)
        rats.append([x1,y1])
        fitness.append(Fun(x1,y1,anchors,d))
    I=fitness.index(min(fitness))
    ratBest=rats[I]
    # print(fitness)
    
    best=fitness[I]
    sorted_fitness = []
    for i in range(n):
        l = [fitness[i],i]
        sorted_fitness.append(l)

    changes=[]
    sorted_fitness.sort()
    # print(sorted_fitness)
    for itr in range(maxIter):
        S = rats
        tmp=rats
        # print(rats)
        
        # Workers phase
        for i in range(breeders, n):
            ab = []
            for j in range(breeders, n):
                ab.append(sorted_fitness[j][1])
            idx = sorted_fitness[i][1]
            lmda = np.random.random()
            random.shuffle(ab)
            S[idx][0] = S[idx][0] + lmda * (S[ab[0]][0] - S[ab[1]][0])
            S[idx][1] = S[idx][1] + lmda * (S[ab[0]][1] - S[ab[1]][1])
            # Calculating and updating new fitness and rat's coordinates
            fnew = Fun(S[idx][0], S[idx][1], anchors, d)
            if fnew < fitness[idx]:
                fitness[idx] = fnew
                rats[idx]= S[idx]
        
        # Breeders phase
        for i in range(breeders):
            if np.random.random() > bp:
                lmda = np.random.random()
                idx = sorted_fitness[i][1]
                
                S[idx][0] = (1-lmda)*S[idx][0] + lmda*(ratBest[0] - S[idx][0])
                S[idx][1] = (1-lmda)*S[idx][1] + lmda*(ratBest[1] - S[idx][1])
                fnew = Fun(S[idx][0], S[idx][1], anchors, d)
                if fnew < fitness[idx]:
                    fitness[idx] = fnew
                    rats[idx]= S[idx]
        
        


        # updating the sorted_fitness list
        sorted_fitness = []
        for i in range(n):
            l = [fitness[i],i]
            sorted_fitness.append(l)
        sorted_fitness.sort()
    
    idr=sorted_fitness[0][1]
        
    
    return rats[idr]
        # print(rats)
    # print(changes)
    # print(fitness)
    
    # new_list=np.array(changes)
    # xt,yt=new_list.T
    # plt.scatter(xt,yt)
    # plt.show()


        
    
anchors = []
anchors.append(sensor('target',0,0))
anchors.append(sensor('target',0,6))
anchors.append(sensor('target',6,0))    
# NMRA(-4,8,-4,8,100,2,10,anchors)