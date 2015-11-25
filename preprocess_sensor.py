#!usr/bin/python

import os.path
import sys

def readFile(filename):
    with open(filename) as f:
        content = f.read().splitlines()
    f.close()
    return content

def writeFile(content, filename):
    output = open(filename,'w')
    for line in content:
        entries = line.split(",")
        if entries[-1] == "Sharp-Right-Turn":
            output.write(line)
            output.write("\n")
        elif entries[-1] == "Move-Forward":
            output.write(line)
            output.write("\n")
    return

if len(sys.argv) < 3:
    print "Please provide necessary files."
else:
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]

    content = readFile(inputfile)
    writeFile(content, outputfile)
