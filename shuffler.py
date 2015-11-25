#!/usr/bin/python

import os.path
import sys
from random import *

def readFile(filename):
    with open(filename) as f:
        content = f.read().splitlines()
    f.close()
    return content

def writeFile(content, filename):
    output = open(filename,'w')
    for line in content:
        output.write(line)
        output.write("\n")
    output.close()
    return

if len(sys.argv) < 3:
    print "Please provide an input and output file." #check for correct usage                        
else:
    inputFilename = sys.argv[1]
    outputFilename = sys.argv[2]
    if not os.path.isfile(inputFilename):
        print "Input file does not exist." #check that input file is real                 
    else:
        content = readFile(inputFilename)
        shuffle(content)
        writeFile(content, outputFilename)
