import math, time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import random
class sensor:
    def __init__(self, type, x, y, x_e = 0, y_e = 0):
        self.type = type
        self.x = x
        self.y = y
        self.x_e = x_e
        self.y_e = y_e
    
    def distance(self, sensor2):
        return math.dist([self.x, self.y], [sensor2.x, sensor2.y])
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
virtual_anchors=find_virtual_anchors(anchor1.x,anchor1.y,3)
virtual_anchors=np.array(virtual_anchors)
x,y=virtual_anchors.T

target_nodes=[]

x_target=np.random.uniform(0,15,5)
y_target=np.random.uniform(0,15,5)

for i in range(5):
    target=sensor('target',x_target[i],y_target[i])
    target_nodes.append(target)


fig,ax=plt.subplots()
ax.scatter(x,y)
ax.set_xlim([0,15])
ax.set_ylim([0,15])
def update(i):
    global x_target
    global y_target,x,y
    
    for i in range(5):
        x_target[i]+=0.1*np.random.randint(-10,10)
        y_target[i]+=0.1*np.random.randint(-10,10)
        if x_target[i]<0 or x_target[i]>15:
            x_target[i]=random.randint(0,15)
        if y_target[i]<0 or y_target[i]>15:
            y_target[i]=random.randint(0,15)
    
    for i in range(5):
        d=math.dist([x_target[i],y_target[i]],[anchor1.x,anchor1.y]);
        virtual_anchors=find_virtual_anchors(anchor1.x,anchor1.y,d)
        virtual_anchors=np.array(virtual_anchors)
        x,y=virtual_anchors.T 
        
       

       
    plt.cla()
    ax.set_xlim([0,15])
    ax.set_ylim([0,15])
    ax.scatter([7.5],[7.5],c='yellow')
    ax.scatter(x,y)
    ax.scatter(x_target,y_target)
    plt.pause(1)
    
ani=FuncAnimation(fig=fig,func=update,interval=5)    
plt.show()


      

    
    

