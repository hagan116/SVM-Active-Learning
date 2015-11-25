#!usr/bin/python

from sklearn import svm
from file_splitter import FileSplitter
from formatter import Formatter
import numpy as np
from scipy.sparse import vstack

class Trainer:

    inputFilename = ""
    outputFilename = ""
    flag = ""

    def __init__(self,inputFile,outputFile,f):
        self.inputFilename = inputFile
        self.outputFilename = outputFile
        self.flag = f
        

    def train(self):
        output = open(self.outputFilename,'w')
        output_confusion = open("confusionMatrix.txt",'w')
        accuracyList = []
        precisionList = []
        recallList = []
        fMeasureList = []
        if self.flag == "-r":
            random = True
            distance = False
            diversity = False
            probability = False
        elif self.flag == "-d":
            random = False
            distance = True
            diversity = False
            probability = False
        elif self.flag == "-v":
            random = False
            distance = False
            diversity = True
            probability = False
        elif self.flag == "-p":
            random = False
            distance = False
            diversity = False
            probability = True
        for i in range(0,5):#run 5 times to obtain an average
            mySplitter = FileSplitter(self.inputFilename)
            if self.inputFilename == "shuffled_magic04.data": #declare a classifier with best parameters for dataset
                clf = svm.SVC(gamma=.01, C=100.0)
            elif self.inputFilename == "ionosphereShuffle.txt":
                clf = svm.SVC(gamma=0.10000000000000001, C=1.0)
            elif self.inputFilename == "sensorShuffled.data":
                clf = svm.SVC(gamma=.01, C=100.0)
            elif self.inputFilename == "mushroom.data":
                clf = svm.SVC(gamma=.10000000000000001, C=1.0)
            trainContent = []
            trainTracker = 0
            accuracyIteration = []
            precisionIteration = []
            recallIteration = []
            fMeasureIteration = []
            for j in range(0,10):
                trainTracker += 1
                if j == 0: 
                    trainContent.extend(mySplitter.removeInitialFive())
                elif (j == 1) or (j == 2):
                    remainingContent = mySplitter.getContent()
                    if self.inputFilename == "shuffled_magic04.data":
                        x2, y2 = Formatter.separate_magic(remainingContent)
                        dec = clf.decision_function(x2)
                    elif self.inputFilename == "ionosphereShuffle.txt":
                        x2, y2 = Formatter.separate_ionosphere(remainingContent)
                        dec = clf.decision_function(x2)
                    elif self.inputFilename == "sensorShuffled.data":
                        x2, y2 = Formatter.separate_sensor(remainingContent)
                        dec = clf.decision_function(x2)
                    elif self.inputFilename == "mushroom.data":
                        x2, y2 = Formatter.separate_mushroom(remainingContent)
                        dec = clf.decision_function(x2)
                    if random == True:
                        trainContent.extend(mySplitter.removeRandom(.025))
                    elif distance == True:
                        trainContent.extend(mySplitter.removeClosest(dec,.025))
                    elif diversity ==  True:
                        trainContent.extend(mySplitter.removeBrinkers(dec,0.85,.025))
                    elif probability == True:
                        trainContent.extend(mySplitter.removeProbable(dec,.025))
                else:
                    remainingContent = mySplitter.getContent()
                    if self.inputFilename == "shuffled_magic04.data":
                        x2, y2 = Formatter.separate_magic(remainingContent)
                        dec = clf.decision_function(x2)
                    elif self.inputFilename == "ionosphereShuffle.txt":
                        x2, y2 = Formatter.separate_ionosphere(remainingContent)
                        dec = clf.decision_function(x2)
                    elif self.inputFilename == "sensorShuffled.data":
                        x2, y2 = Formatter.separate_sensor(remainingContent)
                        dec = clf.decision_function(x2)
                    elif self.inputFilename == "mushroom.data":
                        x2, y2 = Formatter.separate_mushroom(remainingContent)
                        dec = clf.decision_function(x2)
                    if random == True:
                        trainContent.extend(mySplitter.removeRandom(.1))
                    elif distance == True:
                        trainContent.extend(mySplitter.removeClosest(dec,.1))
                    elif diversity ==  True:
                        trainContent.extend(mySplitter.removeBrinkers(dec,0.85,.1))
                    elif probability == True:
                        trainContent.extend(mySplitter.removeProbable(dec,.1))
                
                if self.inputFilename == "shuffled_magic04.data":
                    x1,y1 = Formatter.separate_magic(trainContent) #attributes are stored in x, labels in y
                    predictContent = mySplitter.getTestContent()
                    x2,y2 = Formatter.separate_magic(predictContent)
                elif self.inputFilename == "ionosphereShuffle.txt":
                    x1,y1 = Formatter.separate_ionosphere(trainContent)
                    predictContent = mySplitter.getTestContent()
                    x2,y2 = Formatter.separate_ionosphere(predictContent)
                elif self.inputFilename == "sensorShuffled.data":
                    x1,y1 = Formatter.separate_sensor(trainContent)
                    predictContent = mySplitter.getTestContent()
                    x2,y2 = Formatter.separate_sensor(predictContent)
                elif self.inputFilename == "mushroom.data":
                    x1,y1 = Formatter.separate_mushroom(trainContent)
                    predictContent = mySplitter.getTestContent()
                    x2,y2 = Formatter.separate_mushroom(predictContent)

                clf.fit(x1,y1) #train the classifier with a labeled set
                prediction = clf.predict(x2) #predict the labels for the x2 set, and store them in a variable
                accuracy, precision, recall = Formatter.confusion_matrix(prediction, y2, output_confusion, j)
                fMeasure = Formatter.f_measure(precision,recall)
                accuracy *= 100
                precision *= 100
                recall *= 100
        
                print ("Accuracy: " + str(accuracy) + "%")
                print ("Precision: " + str(precision) + "%")
                print ("Recall: " + str(recall) + "%")
                print ("F-measure: " + str(fMeasure))
            
                fMeasureIteration.append(fMeasure)
                accuracyIteration.append(accuracy)
                precisionIteration.append(precision)
                recallIteration.append(recall)
            fMeasureList.append(fMeasureIteration)
            accuracyList.append(accuracyIteration)
            precisionList.append(precisionIteration)
            recallList.append(recallIteration)
        outputList = Formatter.takeAverage(fMeasureList)
        Formatter.writeHistogramOutput(outputList,output)
        output.close()
        output_confusion.close()

    
