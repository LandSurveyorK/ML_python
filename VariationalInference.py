import numpy as np
from numpy import *
import matplotlib.pyplot as plt

def getX(mu0,sigma2,K,N):
    # create data, specify p(mu,z,x)
    mu = mat(random.normal(mu0,sigma2,(K,1)))
    z = np.random.multinomial(size = N,n = 1, pvals = [1.0 / K]*K)
    xmean =sum(z*mu,axis = 1)
    xvar = ones((N,1))
    x = mat(random.normal(xmean,xvar,(N,1)))
    return x
    # initialize q(mu,z)
def Sampling(mu0,sigma2,K,N,num):
    Pi = (1.0 / K) * mat(ones((K,1)))
    x = getX(mu0,sigma2,K,N)
    ExpeMu = mat(zeros((K,1)))
    VarMu = mat(ones((K,1)))
    q =  mat(ones((N,1))) * Pi.T 
    
    iternum = num 
    while(iternum > 1):
        for i in range(N):
            for k in range(K): 
                q[i,k] = exp( log(Pi[k]) + x[i]* ExpeMu[k] - 0.5*(ExpeMu[k] * ExpeMu[k] + VarMu[k]) )
        q = multiply(q,1.0/sum(q,axis = 1))
        for k in range(K):
            VarMu[k] = 1.0 / (1.0 / sigma2 + sum(q[:,k]))
            ExpeMu[k] = ( mu0 / sigma2 + q[:,k].T * x ) / ( 1.0 / sigma2 + sum(q[:,k]))
        iternum = iternum - 1 
       # ELBO = 0 
       # for k in range(K):
       #     ELBO = ELBO -0.5 * log(2*pi*sigma2)- (ExpeMu[k]^2+VarMu[k] + mu0^2) / (2*sigma2) + ExpeMu[k]*mu0/sigma2
       #     ELBO = ELBO + 0.5 * log(2*pi* (ExpeMu[k]^2 + VarMu[k])) + 0.5
       # for i in range(N):
       #     ELBO = ELBO + log(1.0/K) - q[i,:] * log(q[i,:]).T + 
    return 

    
    
        
    
                         
            
    
    
    