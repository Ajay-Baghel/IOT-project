for i in range(5):
    #     d=math.dist([x_target[i],y_target[i]],[anchor1.x,anchor1.y]);
    #     virtual_anchors=find_virtual_anchors(anchor1.x,anchor1.y,d)
    #     va_dist=[]
    #     for j in range(len(virtual_anchors)):
    #         dist=math.dist([x_target[i],y_target[i]],[virtual_anchors[j][0],virtual_anchors[j][1]])
    #         l=[dist,j]
    #         va_dist.append(l)
    #     va_dist.sort()
    #     idx1,idx2=va_dist[0][1],va_dist[1][1]
    #     va1,va2=virtual_anchors[idx1],virtual_anchors[idx2]
    #     centeroid_x,centeroid_y=(va1[0]+va2[0]+anchor1.x)/3,(va1[1]+va2[1]+anchor1.y)/2