
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

    #For each hyperplane to generate
    for filename in os.listdir(hyperplaneDirectory+'/normalized'):
        nFile = open(hyperplaneDirectory+'/normalized/'+filename, 'r').readlines()[0].split()




        ##### Notation is for shortcuts, which may be used in the future when checking things or changing the way the origin works (or example it'd probably be better to have a stationary origin that doesn't depend on the plane for the future when on-the-fly rotation is attempted.)

        #####----Notation is for simplifications, where we cancel out some calculations in the higher axes which are not needed.


        print("Generating for  "+filename)
        
        a = float(nFile[0])
        b = float(nFile[1])
        c = float(nFile[2])
        d = float(nFile[3])
        e = float(nFile[4])

        ######Create a new origin
        #####xo = (-a*e)/(a**2+b**2+c**2+d**2)
        #####yo = (-b*e)/(a**2+b**2+c**2+d**2)
        #####zo = (-c*e)/(a**2+b**2+c**2+d**2)
        #####wo = (-d*e)/(a**2+b**2+c**2+d**2)
        #####
        #####print("Origin")
        #####print(str(xo))
        #####print(str(yo))
        #####print(str(zo))
        #####print(str(wo))


        #Get new equidistant point to determine y plane from
        x1=(-a*b-a*e)/(a**2+b**2+c**2+d**2)
        y1=(a**2+c**2+d**2-b*e)/(a**2+b**2+c**2+d**2)
        z1=(-b*e-c*e)/(a**2+b**2+c**2+d**2)
        w1=(-b*d-d*e)/(a**2+b**2+c**2+d**2)

        print("Point equidistant to y axis from origin")
        print(str(x1))
        print(str(y1))
        print(str(z1))
        print(str(w1))

        ##############Get the vector perpendicular to the y axis
        #############
        #############Ay=x1-xo
        #############By=y1-yo
        #############Cy=z1-zo
        #############Dy=w1-wo
        #############
        #############print("Vector perpendicular to the y axis")
        #############
        #############print(str(Ay))
        #############print(str(By))
        #############print(str(Cy))
        #############print(str(Dy))

        # Get the vector perpendicular to the y axis

        Ay=(-a*b)/(a**2+b**2+c**2+d**2)
        By=(a**2+c**2+d**2)/(a**2+b**2+c**2+d**2)
        Ay=(-c*b)/(a**2+b**2+c**2+d**2)
        Dy=(-d*b)/(a**2+b**2+c**2+d**2)
        

        print("Vector perpendicular to the y axis")

        print(str(Ay))
        print(str(By))
        print(str(Cy))
        print(str(Dy))
#
#_
#
#Ay=(-ab)/(aa+bb+cc+dd)
#By=(aa+cc+dd)/(aa+bb+cc+dd)
#Cy=(-cb)/(aa+bb+cc+dd)
#Dy = (-db)/(aa+bb+cc+dd)
#
#Simplify
#
#Ay=-ab
#By=aa+cc+dd
#Cy=-cb
#Dy=-db
#
#_
#
#Get vector of new x axis:
#<Ax,Bx,Cx,Dx>
#
#Axa+Bxb+Cxc+Dxd=0
#AxAy+BxBy+CxCy+DxDy=0
#
#Let Ax=1 ^ Dx=1
#
#a+bBx+cCx+d=0
#-ab+aaBx+ccBx+ddBx-cbCx-db=0
#
#Bx=(ab+db+cbCx)/(aa+cc+dd)=b(ab+db+cbCx)/b(aa+cc+dd)
#Bx=(-a-d-cCx)/b=(aa+cc+dd)(-a-d-cCx)/b(aa+cc+dd)
#
#cccCx+aacCx+cddCx+cbbCx=-aaa-aad-acc-ccd-add-ddd-abb-dbb
#
#Cx=(-a-d)(aa+bb+cc+dd)/(ccc+aac+cdd+cbb)
#Cx=(-a-d)/c
#
#Bx=-a-d-c((-a-d)/c))=-a-d+a+d
#Bx=0
#
#Ax=1
#Bx=0
#Cx=(-a-d)/c
#Dx=1
#
#_
#
#Get vector of new z axis:
#<Az,Bz,Cz,Dz>
#
#Aza+Bzb+Czc+Dzd=0
#AzAy+BzBy+CzCy+DzDy=0
#AzAx+BzBx+CzCx+DzDx=0
#
#Let Az=1
#
#https://www.wolframalpha.com/input?i=systems+of+equations+calculator&assumption=%7B%22F%22%2C+%22SolveSystemOf3EquationsCalculator%22%2C+%22equation1%22%7D+-%3E%22a%2Bbx%2Bcy%2B%28d%29%28z%29%3D0%22&assumption=%22FSelect%22+-%3E+%7B%7B%22SolveSystemOf3EquationsCalculator%22%7D%7D&assumption=%7B%22F%22%2C+%22SolveSystemOf3EquationsCalculator%22%2C+%22equation2%22%7D+-%3E%22-ab%2Bx%28a%5E2%2Bb%5E2%2Bd%5E2%29-cby-%28%28d%29%28b%29%28z%29%29%3D0%22&assumption=%7B%22F%22%2C+%22SolveSystemOf3EquationsCalculator%22%2C+%22equation3%22%7D+-%3E%221%2B0%2B%28y%29%28%28-%28a%2Bd%29%29%2Fc%29%2Bz%3D0%22
#
#Az=1
#Bz=0
#Cz=(c(d-a))/(d(a+d)+cc)
#Dz=(ad-aa+cc)/(d(a+d)+cc)
#
#
#
        