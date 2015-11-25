#!usr/bin/python

import os.path
import sys

def readFile(filename):
    with open(filename) as f:
        content = f.read().splitlines()
    f.close()
    return content

def writeFile(content1,content2,content3,content4,outputfile):
    output = open(outputfile,'w')
    for i in range(0,len(content1)):
        output.write(content1[i])
        output.write(" ")
        output.write(content2[i])
        output.write(" ")
        output.write(content3[i])
        output.write(" ")
        output.write(content4[i])
        output.write("\n")
    output.close()
    return

if len(sys.argv) < 6:
    print "Please provide all necessary files."
else:
    random_file = sys.argv[1]
    distance_file = sys.argv[2]
    diversity_file = sys.argv[3]
    probability_file = sys.argv[4]
    output_file = sys.argv[5]

    random_content = readFile(random_file)
    distance_content = readFile(distance_file)
    diversity_content = readFile(diversity_file)
    probability_content = readFile(probability_file)

    writeFile(random_content,distance_content,diversity_content,probability_content,output_file)

    
