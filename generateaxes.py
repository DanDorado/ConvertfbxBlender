
## Command to make the file run ##
#
# generateaxes.py -- 1 1
#
## ARGV ##
#ARGV[0] - Normalize the hyperplanes 1=YES 0=NO
#ARGV[1] - Convert obj files into STL files 1=YES 0=NO
#ARGV[2] - Convert stl files into a spl4 file 1=YES 0=NO
#

import math
import os
import sys

## Values that could change ##
# Directory that raw and normalized hyperplanes are stored inside
hyperplaneDirectory = '/home/dandorado/blender/hyperplanes'


# Get the arguments and save as strings
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"
print(argv)


######### Correct any hyperplanes which become singularities in my method (could also be done by using a seperate set of equations in those cases, but think its no big deal)
if (argv[0] == '1'):
    print("Correct Hyperplanes")
    # For each fbx animation.
    for filename in os.listdir(hyperplaneDirectory):
        
        oFile = open(hyperplaneDirectory+'/'+filename, 'r').readlines()[0].split()
        
        a = float(oFile[0])
        b = float(oFile[1])
        c = float(oFile[2])
        d = float(oFile[3])

        if(c==0):
            c=0.0001
        if(((a**2)+2*(b**2)+(d**2))==0):
            a=a*1.0001
        if((d*(a+d)+c**2)==0):
            c=c*1.0001


        parts=[a,b,c,d]

        nFile = open(hyperplaneDirectory+'/'+filename, 'w+')

        for part in parts:
            print(f'{part:f}')
            nFile.write(str(f'{part:f}')+' ')

        nFile.close()


######## Generate full axes for each hyperplane ##########

if (argv[1] == '1'):
    print("Generating new axes for each hyperplane")

    #For each hyperplane to generate
    for filename in os.listdir(hyperplaneDirectory):
        print(filename)
        nFile = open(hyperplaneDirectory+'/'+filename, 'r').readlines()[0].split()

        print()
        print("Generating for  "+filename)
        print()
        
        a = float(nFile[0])
        b = float(nFile[1])
        c = float(nFile[2])
        d = float(nFile[3])

        # Get the vector perpendicular to the y axis

        Ay=(-a*b)
        By=(a**2+c**2+d**2)
        Cy=(-c*b)
        Dy=(-d*b)
        

        print("Vector perpendicular to the y axis")

        print(str(Ay))
        print(str(By))
        print(str(Cy))
        print(str(Dy))
        print()

        # Get the vector perpendicular to the x axis

        Ax=1
        Bx=0
        Cx=((-a-d)/c)
        Dx=1

        print("Vector perpendicular to the x axis")

        print(str(Ax))
        print(str(Bx))
        print(str(Cx))
        print(str(Dx))
        print()

        # Get the vector perpendicular to the z axis

        print("Vector perpendicular to the z axis")

        Az=1
        Bz=0
        Cz=(c*(d-a))/(d*(a+d)+c**2)
        Dz=(-(a*d)-(a**2)-(c**2))/((d*(a+d))+(c**2))

        print(str(Az))
        print(str(Bz))
        print(str(Cz))
        print(str(Dz))
        print()

        #
        #print("Checking XY / XZ / YZ orthanoganality")
        #print()
        #
        #
        #print("Checking XY")
        #print(str(f'{Ax*Ay:f}'))
        #print(str(f'{Bx*By:f}'))
        #print(str(f'{Cx*Cy:f}'))
        #print(str(f'{Dx*Dy:f}'))
        #print("Checking")
        #print(str(f'{Ax*Ay+Bx*By+Cx*Cy+Dx*Dy:f}'))
        #print()
        #
        #print("Checking XZ")
        #print(str(f'{Ax*Az:f}'))
        #print(str(f'{Bx*Bz:f}'))
        #print(str(f'{Cx*Cz:f}'))
        #print(str(f'{Dx*Dz:f}'))
        #print("Checking")
        #print(str(f'{Ax*Az+Bx*Bz+Cx*Cz+Dx*Dz:f}'))
        #print()
        #
        #print("Checking YZ")
        #print(str(f'{Az*Ay:f}'))
        #print(str(f'{Bz*By:f}'))
        #print(str(f'{Cz*Cy:f}'))
        #print(str(f'{Dz*Dy:f}'))
        #print("Checking")
        #print(str(f'{Az*Ay+Bz*By+Cz*Cy+Dz*Dy:f}'))
        #print()        
        #
        #
        #print("Checking XO")
        #print(str(f'{Ax*a:f}'))
        #print(str(f'{Bx*b:f}'))
        #print(str(f'{Cx*c:f}'))
        #print(str(f'{Dx*d:f}'))
        #print("Checking")
        #print(str(f'{Ax*a+Bx*b+Cx*c+Dx*d:f}'))
        #print()
        #
        #print("Checking YO")
        #print(str(f'{Ay*a:f}'))
        #print(str(f'{By*b:f}'))
        #print(str(f'{Cy*c:f}'))
        #print(str(f'{Dy*d:f}'))
        #print("Checking")
        #print(str(f'{Ay*a+By*b+Cy*c+Dy*d:f}'))
        #print()
        #
        #print("Checking ZO")
        #print(str(f'{Az*a:f}'))
        #print(str(f'{Bz*b:f}'))
        #print(str(f'{Cz*c:f}'))
        #print(str(f'{Dz*d:f}'))
        #print("Checking")
        #print(str(f'{Az*a+Bz*b+Cz*c+Dz*d:f}'))
        #print()


        # Set the axes we need to save
        oPlane=[a,b,c,d]
        xAxis=[Ax,Bx,Cx,Dx]
        yAxis=[Ay,By,Cy,Dy]
        zAxis=[Az,Bz,Cx,Dz]

        writeThings=[oPlane,xAxis,yAxis,zAxis]

        #Save as the final file, which adds the axes to the hyperplane file
        nFile = open(hyperplaneDirectory+'/'+filename, 'w+')

        for parts in writeThings:
            for part in parts:
                print(f'{part:f}')
                nFile.write(str(f'{part:f}')+' ')
            nFile.write("\n")

        nFile.close()
        