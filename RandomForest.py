'''
Created on 2017Äê1ÔÂ19ÈÕ

@author: WEI
'''
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

def subsetSampling
def Bestsplitting
def decisionTree
def Randomforest(filename1,filename2, numTrees, sampleSize, numleaves):
    labelpredict = [];
    for i in range(numTrees):
        dataMat, labelMat = loadDataSet(filename1)
        testdataMat, testlabelMat = loadDataSet(filename2)
        Data = [dataMat :labelMat]
        X,Y = subsetSampling(Data)
        labelpredict.concatenate(labelpredict,(decisionTree(X,Y, testdataMat)), axis = 1)
    return 
        
        
    