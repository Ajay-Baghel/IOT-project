import numpy as np
from sympy.stats import Levy
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
      t=Lb+(Ub-Lb)*np.random.randn(d)
      NMRSolution[i]=t
      NMRfitness[i]=Fun(NMRSolution[i])
    I=np.argmin(NMRfitness)
    fmin=NMRSolution[I]
    NMRBest=NMRSolution[I]
    S=NMRSolution
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
def Fun(a):
    
    return np.random.rand(1)
bb,NMRBest,fmin=NMRA(100,-100,2,Fun,5,30)   
print(bb)
