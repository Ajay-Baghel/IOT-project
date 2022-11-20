import math, time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import random
from nmraNew import *
import copy

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
def find_virtual_anchors(x,y,d):
    anchors=[]
    anchors.append([x+d*np.cos(np.pi/3),y+d*np.sin(np.pi/3)])
    anchors.append([x+d,y])
    anchors.append([x-d,y]);
    anchors.append([x+d*np.cos(np.pi/3),y-d*np.sin(np.pi/3)]);
    anchors.append([x-d*np.cos(np.pi/3),y-d*np.sin(np.pi/3)]);
    anchors.append([x-d*np.cos(np.pi/3),y+d*np.sin(np.pi/3)]);
    return anchors



# Central anchor node
anchor1 = sensor('anchor',7.5,7.5)

# finding virtual anchors
virtual_anchors=find_virtual_anchors(anchor1.x,anchor1.y,4.5)
virtual_anchors=np.array(virtual_anchors)
x,y=virtual_anchors.T

target_nodes=[]

x_target=np.random.uniform(0,15,1)
y_target=np.random.uniform(0,15,1)
# target nodes list
for i in range(len(x_target)):
    target=sensor('target',x_target[i],y_target[i])
    target_nodes.append(target)

# plotting graph for virtual and target nodes

fig,ax=plt.subplots()
scatter=ax.scatter(x,y)
# fig1,ax1=plt.subplots()
ax.set_xlim([0,15])
ax.set_ylim([0,15])
def update(itr):
    global x_target
    global y_target,x,y
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
        d=math.dist([x_target[i],y_target[i]],[anchor1.x,anchor1.y]);
        virtual_anchors=find_virtual_anchors(anchor1.x,anchor1.y,d)
        va_dist=[]
        for j in range(len(virtual_anchors)):
            dist=math.dist([x_target[i],y_target[i]],[virtual_anchors[j][0],virtual_anchors[j][1]])
            l=[dist,j]
            va_dist.append(l)
        va_dist.sort()
        idx1,idx2=va_dist[0][1],va_dist[1][1]
        va1,va2=virtual_anchors[idx1],virtual_anchors[idx2]
        centeroid_x,centeroid_y=(va1[0]+va2[0]+anchor1.x)/3,(va1[1]+va2[1]+anchor1.y)/3
        coordiantes=NMRA(centeroid_x-1,centeroid_x+1,centeroid_y-1,centeroid_y+1,10,3,30,[[anchor1.x,anchor1.y],va1,va2],[x_target[i],y_target[i]])
        print(int(coordiantes[0]),int(coordiantes[1]),int(x_target[i]),int(y_target[i]))
        changes.append(math.dist([coordiantes[0],coordiantes[1]],[x_target[i],y_target[i]]))
    # print("hello")   
    plt.cla()
    ax.set_xlim([0,15])
    ax.set_ylim([0,15])
    ax.scatter([7.5],[7.5],c='yellow')
    ax.scatter(x,y)
    ax.scatter(x_target,y_target,marker='^')
    
    
ani=FuncAnimation(fig=fig,func=update,interval=1000)   

plt.show()




