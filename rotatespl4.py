
## Command to make the file run ##
#
# rotatespl4.py -- 1 1 1
#
## ARGV ##
#ARGV[0] - Normalize the hyperplanes 1=YES 0=NO
#ARGV[1] - Convert obj files into STL files 1=YES 0=NO
#ARGV[2] - Convert stl files into a spl4 file 1=YES 0=NO
#

import math
import os
import re
import sys

## Values that could change ##
# Directory that raw and normalized hyperplanes are stored inside
hyperplaneDirectory = '/home/dandorado/blender/hyperplanes'


# Get the arguments and save as strings
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"
print(argv)

######## Normalize Hyperplanes ##########

if (argv[0] == '1'):
    print("Normalizing+Correct Hyperplanes")
    # For each fbx animation.
    for filename in os.listdir(hyperplaneDirectory+'/originals'):
        nFile = open(hyperplaneDirectory+'/normalized/'+filename, 'w+')
        oFile = open(hyperplaneDirectory+'/originals/'+filename, 'r').readlines()[0].split()
        
        a = float(oFile[0])
        b = float(oFile[1])
        c = float(oFile[2])
        d = float(oFile[3])
        e = float(oFile[4])

        if(c==0):
            c=0.0001
        if(((a**2)+2*(b**2)+(d**2))==0):
            a=a*1.0001
        if((d*(a+d)+c**2)==0):
            c=c*1.0001
        
        length=math.sqrt(a**2+b**2+c**2+d**2)

        print(length)

        normalizelist=[a,b,c,d,e]

        for part in normalizelist:
            part=part/length
            print(f'{part:f}')
            nFile.write(str(f'{part:f}')+' ')



######## Generate full axes for each hyperplane ##########

if (argv[1] == '1'):
    print("Generating new axes for each hyperplane")
    for filename in os.listdir(hyperplaneDirectory+'/normalized'):
        nFile = open(hyperplaneDirectory+'/normalized/'+filename, 'r').readlines()[0].split()
        
        a = float(nFile[0])
        b = float(nFile[1])
        c = float(nFile[2])
        d = float(nFile[3])
        e = float(nFile[4])

        