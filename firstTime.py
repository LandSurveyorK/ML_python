from numpy import *
import matplotlib.pyplot as plt
import matplotlib.image as img
#C:\Users\WEI\workspace\digitsTrain.txt
# Jolie = im.imread('C:\Users\WEI\workspace\jolie.png')
# plt.imshow(Jolie)
# plt.imshow(Jolie,camp='Greys_r')
# plt.imshow(a,cmap='Greys_r')
# plt.show()
import operator
# LOAD DATA
def loadDataSet(filename):
    dataMat =[]; labelMat =[]
    fr = open(filename)
    for line in fr.readlines():
        lineArr = line.strip().split(',')
        fltLine = map(float,lineArr)
        dataMat.append(fltLine[0:-1])
        labelMat.append(float(lineArr[-1]))
    return mat(dataMat),mat(labelMat).T 
# showing the digits (0-9)
def CNNwarmingup(dataMat):
    [n,m] = shape(dataMat)
    sqrt_m = sqrt(m)
    f,ax = plt.subplots(2,5)
    Ind = 0
    while(Ind < 10):
        i = Ind / 5
        j = Ind - i * 5
        position = Ind * 300 +1
        curr = reshape(dataMat[position,:],(sqrt_m,sqrt_m))
        ax[i,j].imshow(curr,cmap='Greys_r',interpolation='nearest')
        ax[i,j].axis('off')
        Ind = Ind + 1
    plt.show     
# softmax fucntion to get probability 
def CNNsoftmax(A):
    [n,m] = shape(A)
    f = mat(zeros((n,m)))
    for j in range(m):
        for i in range(n):
            f[i,j] = exp(A[i,j])
        f[:,j] = f[:,j] / sum(f[:,j])
    return f

def CNNinitial(h, sd):
    # h 784 -> 100 - >10 the framework 
    random.seed(sd)
    numLayers = shape(h)[0]-1
    W = []
    B = []
    for i in range(numLayers):
        b = sqrt(6) / sqrt(h[i]+h[i+1])
        W.append( mat(random.uniform(-b, b, (h[i+1],h[i]))) )
        B.append( mat( zeros( ( h[i+1],1) ) ) )
    return W, B
# CROSS ENTROPY ERROR
def CNNError(W,B,numLayers,dataMat,labelMat):
    A = []; H = []
    H.append(dataMat.T)
    n = shape(dataMat)[0]
    r = 0; count = 0
    for l in range(numLayers):
        A.append(W[l]*H[l]+B[l]*mat(ones((1,n))))
        H.append(sigmoidFunction(A[l]))
    f = CNNsoftmax(A[numLayers-1])
    for i in range(n):
        r = r - log( f[int(labelMat[i]),i]) #MATRIX A[i,j]
        if not_equal(argmax( f[:,i] ), labelMat[i]):
            count = count + 1
    return 1.0 * r / n , 1.0 * count / n
    # crossentropy error , classification error
    # softmax -sum_k (x_klog(x'_k)- (1-x_k)log(1-x'_k) )
    
def CNNBP(seed,alpha,numHiddenUnits,numBatch,numEpoch):
    W,B = CNNinitial(numHiddenUnits,seed)
    numLayers = shape(numHiddenUnits)[0] - 1
    trainDataMat, trainLabelMat = loadDataSet('C:\Users\WEI\workspace\digitsTrain.txt')
    validDataMat, validLabelMat = loadDataSet('C:\Users\WEI\workspace\digitsvalid.txt')
    trainErr = []
    validErr = []
    n = shape(trainDataMat)[0]
    X = trainDataMat; Y = trainLabelMat
    batchSize = n / numBatch
    for epoch in range(numEpoch):
        for ind in range(numBatch):
            A = []; H = []
            H.append( X[ind*batchSize: (ind+1)*batchSize,:].T)
            for l in range(numLayers): # numLayers = 3
                A.append( W[l]*H[l] + B[l] * mat(ones((1,batchSize))) )#
                H.append(mat( sigmoidFunction(A[l]))) # H[numLayers]= output
            # backward 
            GradA = []; GradH = []
            GradW = []; GradB = []
            GradA.append(CNNsoftmax(A[numLayers-1])) #H[3]
            z = Y[ind*batchSize: (ind+1)* batchSize]
            for i in range(batchSize):
                GradA[0][int(z[i]),i] = GradA[0][int(z[i]),i] - 1
            for l in range(numLayers-1):  # 2 
                    GradW.append(GradA[l]*H[numLayers-1-l].T)
                    GradB.append(sum(GradA[l],1))
                    GradH.append(W[numLayers-1-l].T * GradA[l])
                    Gradsigmoid= multiply( H[numLayers-1-l],mat(ones(shape(H[numLayers-1-l])))-H[numLayers-1-l] )
                    GradA.append(multiply(GradH[l],Gradsigmoid))
            GradW.append(GradA[numLayers-l] * H[0].T)
           # GradB.append(sum(GradA[numLayers-l],1))
            for l in range(numLayers):
                W[numLayers-1-l] = W[numLayers-1-l] - multiply( (alpha / batchSize) , GradW[l])
                B[numLayers-1-l] = B[numLayers-1-l] - multiply( (alpha / batchSize) , GradB[l])           
        
        trainErr.append( CNNError(W,B,numLayers,trainDataMat, trainLabelMat))
        validErr.append( CNNError(W,B,numLayers,validDataMat, validLabelMat))
    trainErr = mat(trainErr)
    validErr = mat(validErr)
    plt.figure(1)
    plt.plot(trainErr[:,0]); plt.plot(validErr[:,0])
    plt.figure(2)
    plt.plot(trainErr[:,1]); plt.plot(validErr[:,1])
    plt.show()
        
    return W,B,trainErr,validErr
                 

##################### RBM & AUTOENCODER
# BINARIZE DATA

def binarize(dataMat):
    [n,m] = shape(dataMat)
    X = mat(zeros((n,m)));
    for i in range(n):
        for j in range(m):
            if dataMat[i][j] <0.5 :
                X[i,j] = 0
            else: 
                X[i,j] = 1
    return X
# INITIALIZE W,b,c
def _int_(num_hidden,num_visible,s):
    random.seed(s)
    b = mat(zeros((num_hidden,1)))
    c = mat(zeros((num_visible,1)))
    z = sqrt(6) / sqrt(num_hidden+num_visible)
    W = mat(zeros((num_hidden,num_visible)))
    for i in range(num_hidden):
        for j in range(num_visible):
            W[i,j] = random.uniform(-z,z)
    return mat(W),b,c
#SIGMOID FUNCTION
def sigmoidFunction(z):
    [n,m] = shape(z)
    g = mat(zeros((n,m)))
    for i in range(n):
        for j in range(m):
            g[i,j] = 1.0 / (1.0 + exp(-z[i,j]))
    return g
#GIBBSSAMPLING 
def GibbsSampling(W,b,c,X,CD):
    GX = X;
    n = shape(X)[1]
    for p in range(CD):
        P_H = sigmoidFunction(W*GX+b*mat(ones((1,n))))
        GH = random.binomial(1,P_H)
        P_X = sigmoidFunction(W.T*GH+c*mat(ones((1,n))))
        GX = random.binomial(1,P_X)
    return GX, P_X
#CROSSENTROPY ERRORRATE
def crossEntropyError(X,P_X):
    [n,m] = shape(X)
    error = 0
    for i in range(n):
        for j in range(m):
            error = error - X[i,j]*log(P_X[i,j])-(1-X[i,j])*log(1-P_X[i,j])
    error = error / (n*m)
    return error
#FEATURE VISULIZATION
def featureLearned(W):
    [n,m] = shape(W)
    sqrt_n = int(sqrt(n))
    sqrt_m = int(sqrt(m))
    f,ax = plt.subplots(sqrt_n,sqrt_n)
    for i in range(sqrt_n):
        for j in range(sqrt_n):
            curr = reshape(W[i*sqrt_n+j,:],(sqrt_m,sqrt_m))
            ax[i,j].imshow(curr,cmap='Greys_r',interpolation='nearest')
            ax[i,j].axis('off')
    plt.show
#RESTRICTED BOLZTMANN MACHINE
def RBM(num_hidden,seed,CD,num_epoch,batchSize):
    rate = 0.1
    trainData, trainLabel = loadDataSet('C:\Users\WEI\workspace\digitstrain.txt')
    validData, validLabel = loadDataSet('C:\Users\WEI\workspace\digitsvalid.txt')
    T = shape(trainData)[0]
    num_batch = T / batchSize
    X = binarize(trainData)
    V = binarize(validData)
    W,b,c = _int_(num_hidden,784,seed)
    trainError = zeros((num_epoch,1));
    validError = zeros((num_epoch,1));
    
    for epoch in range(num_epoch):
        for batch in range(num_batch):
            par_W = mat(zeros((num_hidden,784)))
            par_b = mat(zeros((num_hidden,1)))
            par_c = mat(zeros((784,1)))
            for t in range(batchSize):
                xt = X[t+batch*batchSize,:].T
                xtilde,p_xtidle = GibbsSampling(W,b,c,xt,CD)
                h_xt = sigmoidFunction(b+W*xt)
                h_xtilde = sigmoidFunction(b+W*xtilde)
                par_W += (h_xt*xt.T - h_xtilde*xtilde.T)
                par_b += (h_xt - h_xtilde)
                par_c += (xt - xtilde)
            W += multiply( par_W,rate / batchSize)
            b += multiply(par_b,rate / batchSize)
            c += multiply(par_c,rate / batchSize)
        GX,PX = GibbsSampling(W,b,c,X.T,CD)
        GV,PV = GibbsSampling(W,b,c,V.T,CD)
        trainError[epoch] = crossEntropyError(X.T,PX)
        validError[epoch] = crossEntropyError(V.T,PV)
    return W,b,c,trainError,validError
#CONVERT VECTOR TO MATIRX
def diagonalize(z):
    n = shape(z)[0]
    diagz = mat(zeros((n,n)))
    for i in range(n):
        diagz[i,i] = z[i,0]
    return diagz
#AUTOENCODER & DENOISE-AUTOENCODER
def autoencoder(num_hidden,s,num_epoch,batchSize,denoise):
    rate = 0.1
    trainData, trainLabel = loadDataSet('C:\Users\WEI\workspace\digitstrain.txt')
    validData, validlabel = loadDataSet('C:\Users\WEI\workspace\digitsvalid.txt')
    T = shape(trainData)[0]
    num_batch = T / batchSize
    X = binarize(trainData)
    if denoise > 0 :
        drop_prob = multiply(mat(ones((T,784))),denoise)
        drop = random.binomial(1,drop_prob)
        X = multiply(drop,X)        
    V = binarize(validData)
    W,b,c = _int_(num_hidden,784,s)
    trainError = zeros((num_epoch,1))
    validError = zeros((num_epoch,1))
    
    for epoch in range(num_epoch): 
        for batch in range(num_batch):
            Grad_b = mat(zeros((num_hidden,1)))
            Grad_c =  mat(zeros((784,1)))
            Grad_W = mat(zeros((num_hidden,784)))           
            for t in range(batchSize):
                xt = X[t+batch*batchSize,:].T
                h = sigmoidFunction(W*xt+b)
                hx = sigmoidFunction(W.T*h+c)
                Grad_A = hx - xt 
                # Grad_c = Grad_A
                Grad_c += Grad_A
                Grad_b += diagonalize(h) * (eye(shape(h)[0])-diagonalize(h))*(W * Grad_A)
                #Grad_W1 += Grad_A*h.T
                #Grad_W2 +=  W*Grad_A*diagonalize(h)*(eye(shape(b)[0])-diagonalize(h))*xt.T
                Grad_W += h*Grad_A.T + diagonalize(h)*(eye(shape(h)[0])-diagonalize(h))*(W * Grad_A)*xt.T
            W = W -  multiply(Grad_W , rate/ batchSize)
            b = b -  multiply(Grad_b , rate / batchSize)
            c = c - multiply(Grad_c, rate / batchSize)
        
        HatX = sigmoidFunction( W.T *  sigmoidFunction( W*X.T+b*mat(ones((1,3000))) ) + c*mat(ones((1,3000))) )
        HatV = sigmoidFunction(W.T* sigmoidFunction( W*V.T+b*mat(ones((1,1000))) )+c*mat(ones((1,1000)))  ) 
        trainError[epoch]  = crossEntropyError( X.T,HatX)
        validError[epoch] = crossEntropyError(V.T,HatV)
    return W,b,c,trainError,validError   
 
 
 
 
# Homework 3        
# Deep Boltzmann Machine Learning procedure
def Initialize(s,num_h1,num_h2,M):
    random.seed(s)
    c = mat(zeros((784,1)))
    b1 = mat(zeros((num_h1,1)))
    b2 = mat(zeros((num_h2,1)))
    W1 = mat(random.normal(0,1.0,(784,num_h1)))
    W2 = mat(random.normal(0,1.0,(num_h1,num_h2)))
    sampleV = mat(random.binomial(1,0.5,(784,M)))   # p = 0.5 
    sampleH1 = mat(random.binomial(1,0.5,(num_h1,M)))
    sampleH2 = mat(random.binomial(1,0.5,(num_h2,M)))
    return c,b1,b2,W1,W2,sampleV,sampleH1,sampleH2

def varInference(s,num_h1,num_h2,W1,W2,b1,b2,c,V):
    random.seed(s)
    n= shape(V)[1]
    u1 = mat(zeros((num_h1,n))); u2 = mat(zeros((num_h2,n)))
    for i in range(n):
        u1[:,i] = mat(random.normal(0,1.0,(num_h1,1)))
        u2[:,i] = mat(random.normal(0,1.0,(num_h2,1)))
        step = 10
        while(step > 0):
            u1[:,i] = sigmoidFunction(W1.T * V[:,i] + W2 * u2[:,i] + b1)
            u2[:,i] = sigmoidFunction(W2.T * u1[:,i] + b2)
            step = step - 1 
    return u1, u2

def MCMC(s,W1,W2,b1,b2,c,sampleV,sampleH1,sampleH2):
    random.seed(s)
    M = shape(sampleV)[1]
    p_H1 = sigmoidFunction(W1.T * sampleV + W2 * sampleH2 + b1 * mat(ones((1,M))))
    sampleH1 = mat(random.binomial(1,p_H1))
    p_H2 = sigmoidFunction(W2. T * sampleH1  + b2* mat(ones((1,M))))
    sampleH2 = mat(random.binomial(1,p_H2))
    p_V = sigmoidFunction(W1 * sampleH1 + c * mat(ones((1,M))))
    sampleV = mat(random.binomial(1,p_V))
    return sampleV, sampleH1, sampleH2

def reconProb(s,W1,W2,b1,b2,c,Data,num_h2):
    random.seed(s)
    Data = Data.T
    M = shape(Data)[1]
    H2 = mat(random.normal(0,1.0,(num_h2,M)))
    p_H1 = sigmoidFunction(W1.T * Data + W2 * H2 + b1 * mat(ones((1,M))))
    H1 = random.binomial(1,p_H1)
    p_H2 = sigmoidFunction(W2. T * H1  + b2* mat(ones((1,M))))
    H2 = random.binomial(1,p_H2)
    p_data = sigmoidFunction(W1 * H1 + c * mat(ones((1,M))))
    return p_data.T

def DBM(s,num_h1,num_h2,M,num_epoch,batchSize):
    random.seed(s)
    rate = 0.01
    trainData, trainLabel = loadDataSet('C:\Users\WEI\workspace\digitstrain.txt')
    validData, validlabel = loadDataSet('C:\Users\WEI\workspace\digitsvalid.txt')
    T = shape(trainData)[0]
    num_batch = T / batchSize
    trainData = binarize(trainData)      
    validData = binarize(validData)
    trainError = zeros((num_epoch,1))
    validError = zeros((num_epoch,1))
    
    c,b1,b2,W1,W2,sampleV,sampleH1,sampleH2 = Initialize(s,num_h1,num_h2,M)
    for epoch in range(num_epoch): 
        for batch in range(num_batch):
            V = trainData[batch * batchSize + 1: (batch+1)* batchSize,:].T
            u1, u2 = varInference(s,num_h1,num_h2,W1,W2,b1,b2,c,V)
            sampleV,sampleH1,sampleH2 = MCMC(s,W1,W2,b1,b2,c,sampleV,sampleH1,sampleH2)
            # update parameters
            c = c + multiply(sum(V,axis = 1),rate / batchSize) - multiply(sum(sampleV,axis = 1),rate / M )
            b1 = b1 + multiply(sum(u1,axis = 1),rate / batchSize) - multiply(sum(sampleH1,axis = 1),rate / M )
            b2 = b2 + multiply(sum(u2,axis = 1),rate / batchSize) - multiply(sum(sampleH2,axis = 1),rate / M )
            W1 = W1 + multiply(V * u1.T, rate / batchSize) - multiply(sampleV * sampleH1.T, rate / M)
            W2 = W2 + multiply(u1 * u2.T,rate / batchSize) - multiply(sampleH1 * sampleH2.T, rate / M) 
           
        trainError[epoch] = crossEntropyError(trainData,reconProb(s,W1,W2,b1,b2,c,trainData,num_h2))
        validError[epoch]= crossEntropyError(validData,reconProb(s,W1,W2,b1,b2,c,validData,num_h2))
    return W1,W2,c,b1,b2,trainError,validError
        