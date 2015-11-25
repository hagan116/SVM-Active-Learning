#!usr/bin/python

import os.path
import sys
import numpy as np
from random import *
from operator import itemgetter
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from formatter import Formatter
from scipy.spatial.distance import cosine
from scipy.spatial.distance import cdist
import time

class FileSplitter:
    file = ""
    content = []
    testContent = []
    originalLength = 0
    attributeList = []
    

    def __init__(self,inputFile):
        self.file = inputFile
        with open(self.file) as f:
            lines = f.read().splitlines() #splitlines() gets rid of \n
        f.close()
        self.content = lines
        
        self.originalLength = len(self.content)

        self.testContent = []
        testSize = int(.15 * self.originalLength)
        for i in range(0,testSize):
            self.testContent.append(self.content.pop())
            
        labelList = []
        self.attributeList = []
        if self.file == "mushroom.data":
            self.attributeList, labelList = Formatter.separate_mushroom(self.content)
        else:
            for line in self.content:
                attributes = line.split(",")
                attributes = attributes[:-1]
                self.attributeList.append(attributes)
            self.attributeList = np.array(self.attributeList, dtype=float)

    def resetContent(self):
        with open(self.file) as f:
            lines = f.read().splitlines() 
        f.close()
        self.content = lines
        return

    def getFileName(self):
        return self.file

    def getFileLength(self):
        return len(self.content)

    def getTestContent(self):
        return self.testContent

    def getContent(self):
        return self.content

    def removeInitialFive(self):
        result = []
        limit = int(.05 * self.originalLength)
        for i in range(0,limit):
            result.append(self.content.pop())
            np.delete(self.attributeList,len(self.attributeList)-1,0)
        return result

    def removeRandom(self, percent):
        batchSize = int(percent * self.originalLength)
        result = []
        shuffle(self.content)
        for i in range(0,batchSize):
            result.append(self.content.pop())
        return result
    
    def cosTheta(self,sample1_attributes,sample2_attributes):
        dot_product = np.dot(sample1_attributes,sample2_attributes)#calculate dot product
        mag1 = np.linalg.norm(sample1_attributes)#calculate vector magnitudes
        mag2 = np.linalg.norm(sample2_attributes)
        result = dot_product/(mag1*mag2)#calculate cos(theta)
        return result


    def removeBrinkers(self, dec, lam, percent):
        batchSize = int(percent * self.originalLength)
        result  = []
        maxCos = []
        indexList = set()

        dec = map(abs,dec)

        paired = zip(self.content,dec)
        
        for i in range(0,len(dec)):
            maxCos.append(0)
        for k in range(0,batchSize):
            minIndex = k
            minValue = sys.maxint
            for j in range(0,len(dec)):
                if j in indexList:
                    continue
                value = lam * dec[j] + (1 - lam) * maxCos[j]
                if value < minValue:
                    minIndex = j
                    minValue = value
            result.append(paired[minIndex][0])
            indexList.add(minIndex) 
            l = list()
            l.append(self.attributeList[minIndex])
	    cosangles = map(float,cdist (self.attributeList, l,'cosine')) 

            for j in range(0,len(dec)):
                if j in indexList:
                    continue
                if cosangles[j] > maxCos[j]:
                    maxCos[j] = cosangles[j]
                           
        for entry in result:
            self.content.remove(entry)
        np.delete(self.attributeList,list(indexList), axis=0)
        return result

    def removeDiverse(self, dec, percent):
        batchSize = int(percent * self.originalLength)
        result = []
        dec = map(abs,dec)
        paired = zip(self.content, dec)#pair each line in the content with its distance value
        distance_sorted = sorted(paired,key=itemgetter(1))#sort based on distance
        result.append(distance_sorted[0][0])
        i = 1
        while len(result) < batchSize:#while less than 5% are stored
            dot_values = []
            for j in range(0,i):
                dot_product = self.cosTheta(distance_sorted[j],distance_sorted[i])
                dot_values.append(dot_product)
            average = sum(dot_values)/len(dot_values)
            if average < .99:
                result.append(distance_sorted[i][0])
                i += 1
            else:
                distance_sorted.remove(distance_sorted[i])
            
        for entry in result:
            self.content.remove(entry)#pop the sample from the content and append it to the result array
        return result

    def removeClosest(self, dec, percent):
        batchSize = int(percent * self.originalLength)
        result = []
        dec = map(abs,dec)
        paired = zip(self.content, dec)
        distance_sorted = sorted(paired,key=itemgetter(1))
        for i in range(0,batchSize):
            index = self.content.index(distance_sorted[i][0])
            result.append(self.content.pop(index))
        return result

    def removeProbable(self, dec, percent):
        batchSize = int(percent * self.originalLength)
        result = []
        dec = map(abs,dec)#take the absolute value of the distances
        dec = map(lambda x:float(1/x),dec)#calculate the inverse of the distance
        divisor = sum(dec)#get a divisor for probabilities
        probabilities = map(lambda x:x/divisor,dec)#divide by the divisor to get a probability
        paired = map(list, zip(self.content,probabilities))#associate probabilities with samples, cast to list so it's mutable
        for i in range(1,len(paired)):
            paired[i][1] += paired[i-1][1]#sum each probability with the previous entries
        while len(result) < batchSize:
            rand_value = uniform(0,1.0)
            if rand_value < paired[0][1]:
                result.append(paired[0][0])
                self.content.remove(paired[0][0])
                paired.pop(0)
                continue
            for i in range(1,len(paired)):
                if rand_value >= (paired[i-1][1]) and rand_value < (paired[i][1]):
                    result.append(paired[i][0])
                    self.content.remove(paired[i][0])
                    paired.pop(i)
                    break
                    
        return result
