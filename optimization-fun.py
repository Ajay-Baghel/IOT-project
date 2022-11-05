import math
class sensor:
    def __init__(self, type, x, y, x_e = 0, y_e = 0):
        self.type = type
        self.x = x
        self.y = y
        self.x_e = x_e
        self.y_e = y_e
    
    def distance(self, sensor2):
        return math.dist([self.x, self.y], [sensor2.x, sensor2.y])
    
def optimization_fun(x,y, anchors, d):
    f = 0
    for i in range(3):
        print(anchors[i].x,anchors[i].y )
        f +=  math.pow(math.sqrt(math.pow((x-anchors[i].x),2) + math.pow((y-anchors[i].y),2)) - d,2)
        print(f)
    return f/3

print("hello")
anchors = []
anchors.append(sensor('target',0,0))
anchors.append(sensor('target',0,6))
anchors.append(sensor('target',6,0))
    
print(optimization_fun(2,2,anchors,6))
    