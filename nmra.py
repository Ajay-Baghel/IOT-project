import numpy as np
from sympy.stats import Levy
import math
def Fun(x,y, anchors, d):
    f = 0
    for i in range(3):
        print(anchors[i].x,anchors[i].y )
        f +=  math.pow(math.sqrt(math.pow((x-anchors[i].x),2) + math.pow((y-anchors[i].y),2)) - d,2)
        print(f)
    return f/3
def Fun(i):
    return 0;    
def NMRA(Ub,Lb,d,Fun,maxiter,n):
    bb=[]

    bp=0.5
    breeders=n//5
    workers=n-n/5
    iter=1
    NMRSolution=np.zeros((n,2))
    NMRfitness=np.zeros(n)
    # print(NMRSolution.shape)
    for i in range(n):
      tx=Lb+(Ub-Lb)*np.random.randn()
      ty=Lb+(Ub-Lb)*np.random.randn()
      NMRSolution[i][0]=tx
      NMRSolution[i][1]=ty
      NMRfitness[i]=Fun(NMRSolution[i])
    I=np.argmin(NMRfitness)
    fmin=NMRfitness[I]
    NMRBest=NMRSolution[I]
    S=NMRSolution
    print(NMRSolution)
    while iter<maxiter:
        for i in range(int(workers)):
            lmbda=np.random.randn(0,1)
            ab=np.arange(int(workers))
            np.random.shuffle(ab)
            L=np.random.rand()
            S[i]=NMRSolution[i]+L*((NMRSolution[ab[0]])-NMRSolution[ab[1]])
            Fnew=Fun(S[i])
            
            if Fnew<=NMRfitness[i]:
                NMRSolution[i]=S[i]
                NMRfitness[i]=Fnew
        for z in range(breeders):
            if np.random.rand()>bp:
                # random permute of breeders
               lmbda=np.random.rand(1)
               NMRneighbour=np.arange(n//5)
               np.random.shuffle(NMRneighbour) 
            #    print(S[z].shape)
               S[z]=(1-lmbda)*S[z]+(lmbda*(NMRBest-NMRSolution[NMRneighbour[0]]).reshape(2,))
               Fnew=Fun(S[z])
               if Fnew<=NMRfitness[z]:
                 NMRSolution[z]=S[z]
                 NMRfitness[z]=Fnew
        for i in range(n):
            Flag4Ub=S[i]>Ub
            Flag4Lb=S[i]<Lb
            S[i]=S[i]*(~(Flag4Ub+Flag4Lb))+Ub*Flag4Ub+Lb*Flag4Lb   
    I=np.argmin(NMRfitness)
    fmin=NMRSolution[I]
    NMRBest=NMRSolution[I]
    S=NMRSolution
    bb.append(fmin)
    return [bb,NMRBest,fmin]

bb,NMRBest,fmin=NMRA(100,-100,2,Fun,5,30)   
print(NMRBest)
