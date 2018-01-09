
import scipy
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import random
from scipy.stats import f
from bisect import bisect_left
from scipy.stats import norm

# Covariance Matrix
def covMat(numFeat, covType):
    Sigma0=  mat(eye(numFeat))

    Sigma1 = mat(zeros((numFeat,numFeat)))
    for i in range(numFeat):
        if i < 20:
            Sigma1[i,i] = 20.0 / (i+1)
        else:
            Sigma1[i,i] = 1

    Sigma2 = mat(zeros((numFeat, numFeat)))
    for i in range(numFeat-1):
        Sigma2[i,i] = 1
        Sigma2[i,i+1] = 0.4 ; Sigma2[i+1,i] = 0.4
    Sigma2[numFeat-1, numFeat-1] = 1

    Sigma3 = mat(zeros((numFeat, numFeat)))
    numBlock = int(numFeat / 25)
    B = 0.85 * eye(25) + 0.15 * ones((25,25))
    for k in range(numBlock):
        for i in range(25):
            for j in range(25):
                Sigma3[25*k+i,25*k+j] = B[i,j]
    Sigma = [Sigma0,Sigma1,Sigma2,Sigma3]
    return Sigma[covType]

# Alternatives
def altmu(numFeat, Sigma, percent,altType):
    np.random.seed(7)
    mu1 = mat(zeros((numFeat,1)))
    n = int(numFeat * percent)
    mu2 = mat(np.random.normal(1,1,(numFeat,1)))
    drop = random.sample(range(numFeat),n)
    for i in range(shape(drop)[0]):
        mu2[int(drop[i])] = 0
    scaled0 = multiply(1.0/ sqrt(0.5* mu2.T * Sigma.I*mu2),mu2)
    scaled1 = multiply(1.0 / sqrt( 10 * mu2.T *mu2 / sqrt(trace(Sigma*Sigma)) ), mu2)
    scaled = [scaled0, scaled1]
    mu2 = mat(scaled[altType])
    mu1 = mu1.T ; mu2 = mu2.T
    mu1 = np.squeeze(np.asarray(mu1)); mu1.tolist()
    mu2 = np.squeeze(np.asarray(mu2)); mu2.tolist()
    return mu1, mu2

# Random Projection Matrix
def projMat(numFeat, k):
    r = np.random.normal(0,1,(numFeat,1))
    R = mat(zeros((numFeat,k)))
    Block = int(numFeat / k)
    for j in range(k):
        for i in range(Block):
            R[j*Block+i,j] = r[j*Block+i]
    return R

# Data Simulation
def simData(mu1,mu2,Sigma, n1,n2):
    X = mat(np.random.multivariate_normal(mu1,Sigma,n1))
    Y = mat(np.random.multivariate_normal(mu2,Sigma,n2))
    return X,Y

# p-vlaue Bar
def pvalue(mu1,mu2,Sigma,X,Y,numFeat,k,n1,n2,m,seed):
    np.random.seed(seed)
    theta = 0
    Sx = X.T * ( mat(eye(n1))- 1.0/n1 *mat(ones((n1,n1))) ) * X
    Sy = Y.T * ( mat(eye(n2))- 1.0/n2 *mat(ones((n2,n2))) ) * Y
    n = n1 + n2 - 2
    S = 1.0 / n *(Sx + Sy)
    for i in range(m):
        R = projMat(numFeat,k)
        meanDiff = (mean(X,0) - mean(Y,0)).T
        T2 = (n1 * n2) / (n1 + n2) * meanDiff.T*R* (R.T*S*R).I *R.T* meanDiff
        critVal = 1.0 * (n - k - 1) / k * T2 / n
        theta = theta + (1 - f.cdf(critVal, k, n-k+1) )
    theta = 1.0 * theta / m

    return theta[0][0]

# Emperical Dist of p-value Bar
def simDist(mu1,mu2,Sigma,numFeat,k,n1,n2,m,num):
    # m: num of projection
    # num : num of pvalBar
    # n1, n2 num of x ,y respectively
    thetaList = [];

    for i in range(num):
        seed = i
        X,Y = simData(mu1,mu2,Sigma, n1,n2)
        currTheta = pvalue(mu1,mu2,Sigma,X,Y,numFeat,k,n1,n2,m,seed)
        thetaList.append(currTheta)
    return thetaList



# Find The Critical Value Under the Null Hypothesis
def rejVal(numFeat,k, n1,n2,m,num):
    alpha = 0.05
    Sigma = covMat(numFeat,0)
    mu1 = list(zeros(numFeat))
    mu2 = list(zeros(numFeat))
    thetaList = simDist(mu1,mu2,Sigma,numFeat,k,n1,n2,m,num)
    thetaList_len = len(thetaList)
    return thetaList[int((1-alpha) * thetaList_len)]



 # Plot Emperical CDF
def ecdf(x):
    xs = np.sort(x)
    ys = np.arange(1, len(xs)+1)/float(len(xs))
    return xs, ys

def plotCdf(data,name,rejVal):
    fig = plt.figure()
    xs, ys = ecdf(data)
    plt.plot(xs, ys, label="Empirical", marker=">", markerfacecolor='none')
    plt.plot([rejVal], [0], marker='o', markersize=3, color="red")
    plt.plot((rejVal,rejVal), (0, 1), color='red',linestyle="--")
    fig.savefig(name)




def plotmeanUnif(n,num):
    Y = []
    for k in range(num):
        curr = 0
        for i in range(n):
            curr = curr + np.random.uniform(0,1)
        Y.append(curr / n)
    plotCdf(Y,"cdfmeanUnif")


def run():
    numFeat = 200; covType = 2; k = 40;
    n1=50; n2= 50 ; m = 500; num = 200;
    altType = 0; percent = 0.5;seed = 666;
    Sigma = covMat(numFeat,covType);
    mu1,mu2 = altmu(numFeat,Sigma,percent,altType)
    # X,Y = hello.simData(mu1,mu2,Sigma, n1,n2)
    rV = rejVal(numFeat,k, n1,n2,m,num)
    # hello.pvalue(mu1,mu2,Sigma,X,Y,numFeat,k,n1,n2,m,seed)
    thetaList = simDist(mu1,mu2,Sigma,numFeat,k,n1,n2,m,num)
    plotCdf(thetaList,"empirical dist",rV)
    #hello.plotmeanUnif(100,200)



    
    
         
    
    
    
    
    
        

   
    
    