
## Command to make the file run ##
#
# python3 rotatespacetime.py -- 1
#
## ARGV ##
#ARGV[0] - Generate a single frame or a sequence of frames:
# 0=SINGLE FRAME with 'constant' being taken as e
# 1=FULL FRAMES outputting n frames where n is 'frames' constant. This splits the spl4 shape into n segments out outputs frames from the centre of each.
# 2=FULL FPS outputting a number of frames where the constant is set to the lowest possible (rounded up slightly) and then incremented by 'increment'

import math
import os
import re
import sys

## Values that could change ##
# Directory that raw and normalized hyperplanes are stored inside
hyperplaneDirectory = '/home/dandorado/blender/hyperplanes'
spl4Directory = '/home/dandorado/blender/spl4Objects'
finalSTLs = '/home/dandorado/blender/rotatesSTLs'

constant = 2.5
frames = 10
increment = 1.2

# Get the arguments and save as strings
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"
print(argv)


#########Gets all the necessary details for rotating
print("Begin the conversion")

#For each 
for filename in os.listdir(hyperplaneDirectory):
    print("Starting with "+filename)
    
    hyperplanes = open(hyperplaneDirectory+'/'+filename, 'r').readlines()

    print("Getting hypervectors")

    oPlane = hyperplanes[0].split()
    
    a = float(oPlane[0])
    b = float(oPlane[1])
    c = float(oPlane[2])
    d = float(oPlane[3])

    xAxis = hyperplanes[1].split()
    
    Ax = float(xAxis[0])
    Bx = float(xAxis[1])
    Cx = float(xAxis[2])
    Dx = float(xAxis[3])
        
    yAxis = hyperplanes[2].split()
    
    Ay = float(yAxis[0])
    By = float(yAxis[1])
    Cy = float(yAxis[2])
    Dy = float(yAxis[3])

    zAxis = hyperplanes[3].split()
    
    Az = float(zAxis[0])
    Bz = float(zAxis[1])
    Cz = float(zAxis[2])
    Dz = float(zAxis[3])

    for filename in os.listdir(spl4Directory):

            # Creates a list of the needed spl4 data of the form:
            # prisms[i][0-5][0-4]
            #        ^    ^   ^
            #        |    |   x,y,z,w
            #        |    vertex
            #        prism

            print("Starting with "+filename)
            
            spl4 = open(spl4Directory+'/'+filename, 'r').readlines()

            print(len(spl4))

            i=0
            prisms=[None]*int((len(spl4)/7))
            print(str(len(spl4)/7)+" prisms to consider.")
            while(i<len(spl4)/7):
                print(spl4[7*i]+str(i)+"\n")
                prism=[None]*6
                j=1
                while(j<7):
                    vertex=[spl4[j+(7*i)].split()[1],spl4[j+(7*i)].split()[2],spl4[j+(7*i)].split()[3],spl4[j+(7*i)].split()[4]]
                    #print(vertex)
                    prism[j-1]=vertex
                    j=j+1
                #print(prism)
                prisms[i]=prism
                i=i+1
            #print(prisms[6][5][3])