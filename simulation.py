import math, time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
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
plt.xlim(0,15)
plt.ylim(0,15)
plt.scatter(x,y)
plt.scatter(7.5,7.5,c='pink')





target_nodes=[]

x_target=np.random.uniform(0,15,5)
y_target=np.random.uniform(0,15,5)
plt.scatter(x_target, y_target)

for i in range(5):
    target=sensor('target',x_target[i],y_target[i])
    target_nodes.append(target)


    
# # add mobility
for i in range(10):
    for i in range(5):
        x_target[i]+=0.1*np.random.randint(-10,10)
        y_target[i]+=0.1*np.random.randint(-10,10)
    plt.scatter(x_target,y_target)
    plt.pause(1)
    # plt.remove(x_target,y_target)
plt.show()        

    
    

