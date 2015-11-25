#!usr/bin/python

# various necessary imports
import os.path
import sys
from svm_training import Trainer


########## Main ##########
if len(sys.argv) < 3:
    print "Please provide an input and output file." #check for correct usage
elif len(sys.argv) < 4:
    inputFilename = sys.argv[1]
    outputFilename = sys.argv[2]
    flag = "-r"
    if not os.path.isfile(inputFilename):
        print "Input file does not exist." #check that input file is real
    else:
        trainer = Trainer(inputFilename,outputFilename,flag)
        trainer.train()
else:
    flag = sys.argv[1]
    inputFilename = sys.argv[2]
    outputFilename = sys.argv[3]
    trainer = Trainer(inputFilename,outputFilename,flag)
    trainer.train()
