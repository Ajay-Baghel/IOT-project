import numpy as np
from sympy.stats import Levy
import math
import random
import matplotlib.pyplot as plt
import math, time
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import random
import copy

def find_virtual_anchors(x,y,d):
    anchors=[]
    anchors.append([x+d*np.cos(np.pi/3),y+d*np.sin(np.pi/3)])
    anchors.append([x+d,y])
    anchors.append([x-d,y]);
    anchors.append([x+d*np.cos(np.pi/3),y-d*np.sin(np.pi/3)]);
    anchors.append([x-d*np.cos(np.pi/3),y-d*np.sin(np.pi/3)]);
    anchors.append([x-d*np.cos(np.pi/3),y+d*np.sin(np.pi/3)]);
    return anchors

class sensor:
    def __init__(self, type, x, y, x_e = 0, y_e = 0):
        self.type = type
        self.x = x
        self.y = y
        self.x_e = x_e
        self.y_e = y_e

# Optimization/cost function
def Fun(x,y, anchors, target):
    f = 0
    # return math.dist([x,y],[target[0],target[1]])
    for i in range(3):
        # print(anchors[i].x,anchors[i].y )
        d = math.dist([target[0],target[1]], [anchors[i][0],anchors[i][1]])
        d1= math.dist([x,y],[anchors[i][0],anchors[i][1]])
        f +=  math.pow( abs(d1 - d),2)
        # print(f)
    return f

def NMRA(maxIter,best,n,anchors,target,x,y):
    d=math.dist([x,y],[anchor1.x,anchor1.y]);
    virtual_anchors=find_virtual_anchors(anchor1.x,anchor1.y,d)
    va_dist=[]
    for j in range(len(virtual_anchors)):
        dist=math.dist([x,y],[virtual_anchors[j][0],virtual_anchors[j][1]])
        l=[dist,j]
        va_dist.append(l)
    va_dist.sort()
    idx1,idx2=va_dist[0][1],va_dist[1][1]
    va1,va2=virtual_anchors[idx1],virtual_anchors[idx2]
    centeroid_x,centeroid_y=(va1[0]+va2[0]+anchor1.x)/3,(va1[1]+va2[1]+anchor1.y)/3
    x_lb,x_ub,y_lb,y_ub=centeroid_x-1,centeroid_x+1,centeroid_y-1,centeroid_y+1
    anchors.append(va1)
    anchors.append(va2)
    rats=[]
#     24
    workers=n-n//5 
    #6
    
    breeders=n//5
    fitness=[]
    bp=0.5
   
    rats.append([(x_lb+x_ub)/2,(y_lb+y_ub)/2])
    fitness.append(Fun((x_lb+x_ub)/2,(y_lb+y_ub)/2,anchors,target))
    for i in range(n-1):
        x1=x_lb+np.random.random()*(x_ub-x_lb)
        y1=y_lb+np.random.random()*(y_ub-y_lb)
        rats.append([x1,y1])
        fitness.append(Fun(x1,y1,anchors,target))
    
    sorted_fitness = []
    for i in range(n):
        l = [fitness[i],i]
        sorted_fitness.append(l)
   
    sorted_fitness.sort()
    for itr in range(maxIter):
        S = copy.deepcopy(rats)
        ratBest=rats[sorted_fitness[0][1]]
        
        # Workers phase
        lmda = np.random.random()
        for i in range(breeders, n):
            ab = []
            for j in range(breeders, n):
                ab.append(sorted_fitness[j][1])
            idx = sorted_fitness[i][1]
            
            random.shuffle(ab)
            # print(lmda)
            S[idx][0] = S[idx][0] + lmda * (S[ab[0]][0] - S[ab[1]][0])
            S[idx][1] = S[idx][1] + lmda * (S[ab[0]][1] - S[ab[1]][1])
            # Calculating and updating new fitness and rat's coordinates
            fnew = Fun(S[idx][0], S[idx][1], anchors, target)
            if fnew < fitness[idx]:

                fitness[idx] = fnew
                rats[idx]= S[idx]
        
        # Breeders phase
        for i in range(breeders):
            if np.random.random() > bp:
#                 lmda = np.random.random()
                idx = sorted_fitness[i][1]
                
                S[idx][0] = (1-lmda)*S[idx][0] + lmda*(ratBest[0] - S[idx][0])
                S[idx][1] = (1-lmda)*S[idx][1] + lmda*(ratBest[1] - S[idx][1])
                fnew = Fun(S[idx][0], S[idx][1], anchors, target)
                if fnew < fitness[idx]:

                    fitness[idx] = fnew
                    rats[idx]= S[idx]
        sorted_fitness.clear()
        for i in range(n):
            l = [fitness[i],i]
            sorted_fitness.append(l)
        sorted_fitness.sort()
        idx_graph=sorted_fitness[0][1]
        r=np.array(rats)
        an=np.array(anchors)
        xr,yr=r.T
        xa,ya=an.T
        fig,ax=plt.subplots()
        ax.set_xlim(0,15)
        ax.set_ylim(0,15)
        ax.scatter(xr,yr,marker='^')
        ax.scatter(xa,ya)
        ax.scatter(target[0],target[1])
        ax.scatter(rats[idx_graph][0],rats[idx_graph][1])
        plt.show()
        print(rats[idx_graph])
        print(sorted_fitness[0][0])

    
    idr=sorted_fitness[0][1]
#     print(rats[idr])
    
    return rats[idr]

class sensor:
    def __init__(self, type, x, y, x_e = 0, y_e = 0):
        self.type = type
        self.x = x
        self.y = y
        self.x_e = x_e
        self.y_e = y_e
    
    def distance(self, sensor2):
        return math.dist([self.x, self.y], [sensor2.x, sensor2.y])

# Function to find virtual anchors



# Central anchor node
anchor1 = sensor('anchor',7.5,7.5)

# finding virtual anchors


target_nodes=[]

x_target=np.random.uniform(0,15,1)
y_target=np.random.uniform(0,15,1)
# target nodes list
for i in range(len(x_target)):
    target=sensor('target',x_target[i],y_target[i])
    target_nodes.append(target)
# print(target_nodes)   
    
    
predicted=[]
original=[]
for i in range(1):
    
    changes=[]
    # Adding random movement to the target nodes
    for i in range(len(x_target)):
        x_target[i]+=0.1*random.uniform(-15,15)
        y_target[i]+=0.1*random.uniform(-15,15)
        if x_target[i]<0 or x_target[i]>15:
            x_target[i]=random.uniform(0,15)
        if y_target[i]<0 or y_target[i]>15:
            y_target[i]=random.uniform(0,15)

    for i in range(len(x_target)):
        coordiantes=NMRA(50,3,30,[[anchor1.x,anchor1.y]],[x_target[i],y_target[i]],x_target[i],y_target[i])
        predicted.append(coordiantes)
        original.append([x_target[i],y_target[i]])
print(predicted,original)
