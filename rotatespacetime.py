
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
finalSTLs = '/home/dandorado/blender/rotatedSTLs'

singleConstant = 31000
frames = 50
increment = 1.2

# Get the arguments and save as strings
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"
print(argv)


#########Gets all the necessary details for rotating
print("Begin the conversion")
intersectTriangleTable=[[[[[[[[[3,5],[4,5],[2,5]]]],[[[[1,4],[2,5],[3,5]],[[3,4],[2,5],[3,5]],[[3,4],[1,4],[3,5]],[[3,4],[1,4],[2,5]]]]],[[[[[0,3],[2,5],[4,5]],[[3,4],[2,5],[4,5]],[[3,4],[0,3],[4,5]],[[3,4],[0,3],[2,5]]]],[[[[0,3],[1,4],[2,5]]]]]],[[[[[[1,2],[4,5],[3,5]],[[0,2],[4,5],[3,5]],[[0,2],[1,2],[3,5]],[[0,2],[1,2],[4,5]]]],[[[[1,4],[3,4],[3,5]],[[1,2],[3,4],[3,5]],[[1,2],[1,4],[3,5]],[[1,2],[1,4],[3,4]],[[0,2],[3,4],[3,5]],[[0,2],[1,4],[3,5]],[[0,2],[1,4],[3,4]],[[0,2],[1,2],[3,5]],[[0,2],[1,2],[3,4]],[[0,2],[1,2],[1,4]]]]],[[[[[0,3],[3,4],[4,5]],[[0,2],[3,4],[4,5]],[[0,2],[0,3],[4,5]],[[0,2],[0,3],[3,4]],[[1,2],[3,4],[4,5]],[[1,2],[0,3],[4,5]],[[1,2],[0,3],[3,4]],[[1,2],[0,2],[4,5]],[[1,2],[0,2],[3,4]],[[1,2],[0,2],[0,3]]]],[[[[0,3],[1,4],[1,2]],[[0,2],[1,4],[1,2]],[[0,2],[0,3],[1,2]],[[0,2],[0,3],[1,4]]]]]]],[[[[[[[1,2],[0,1],[1,4]],[[3,5],[4,5],[2,5]]]],[[[[2,5],[3,5],[3,4]],[[1,2],[3,5],[3,4]],[[1,2],[2,5],[3,4]],[[1,2],[2,5],[3,5]],[[0,1],[3,5],[3,4]],[[0,1],[2,5],[3,4]],[[0,1],[2,5],[3,5]],[[0,1],[1,2],[3,4]],[[0,1],[1,2],[3,5]],[[0,1],[1,2],[2,5]]]]],[[[[[1,2],[0,1],[1,4]],[[0,3],[2,5],[1,2]],[[0,1],[2,5],[1,2]],[[0,1],[0,3],[1,2]],[[0,1],[0,3],[2,5]],[[3,4],[4,5],[1,4]],[[0,3],[2,5],[4,5]],[[3,4],[2,5],[4,5]],[[3,4],[0,3],[4,5]],[[3,4],[0,3],[2,5]]]],[[[[0,3],[2,5],[1,2]],[[0,1],[2,5],[1,2]],[[0,1],[0,3],[1,2]],[[0,1],[0,3],[2,5]]]]]],[[[[[[1,4],[4,5],[3,5]],[[0,1],[4,5],[3,5]],[[0,1],[1,4],[3,5]],[[0,1],[1,4],[4,5]],[[0,2],[4,5],[3,5]],[[0,2],[1,4],[3,5]],[[0,2],[1,4],[4,5]],[[0,2],[0,1],[3,5]],[[0,2],[0,1],[4,5]],[[0,2],[0,1],[1,4]]]],[[[[0,2],[3,5],[3,4]],[[0,1],[3,5],[3,4]],[[0,1],[0,2],[3,4]],[[0,1],[0,2],[3,5]]]]],[[[[[0,1],[0,2],[0,3]],[[3,4],[4,5],[1,4]]]],[[[[0,1],[0,2],[0,3]]]]]]]],[[[[[[[[0,1],[0,2],[0,3]],[[3,5],[4,5],[2,5]]]],[[[[0,1],[0,2],[0,3]],[[1,4],[2,5],[0,2]],[[0,1],[2,5],[0,2]],[[0,1],[1,4],[0,2]],[[0,1],[1,4],[2,5]],[[3,4],[3,5],[0,3]],[[1,4],[2,5],[3,5]],[[3,4],[2,5],[3,5]],[[3,4],[1,4],[3,5]],[[3,4],[1,4],[2,5]]]]],[[[[[2,5],[4,5],[3,4]],[[0,2],[4,5],[3,4]],[[0,2],[2,5],[3,4]],[[0,2],[2,5],[4,5]],[[0,1],[4,5],[3,4]],[[0,1],[2,5],[3,4]],[[0,1],[2,5],[4,5]],[[0,1],[0,2],[3,4]],[[0,1],[0,2],[4,5]],[[0,1],[0,2],[2,5]]]],[[[[1,4],[2,5],[0,2]],[[0,1],[2,5],[0,2]],[[0,1],[1,4],[0,2]],[[0,1],[1,4],[2,5]]]]]],[[[[[[0,3],[3,5],[4,5]],[[0,1],[3,5],[4,5]],[[0,1],[0,3],[4,5]],[[0,1],[0,3],[3,5]],[[1,2],[3,5],[4,5]],[[1,2],[0,3],[4,5]],[[1,2],[0,3],[3,5]],[[1,2],[0,1],[4,5]],[[1,2],[0,1],[3,5]],[[1,2],[0,1],[0,3]]]],[[[[1,2],[0,1],[1,4]],[[3,4],[3,5],[0,3]]]]],[[[[[0,1],[3,4],[4,5]],[[1,2],[3,4],[4,5]],[[1,2],[0,1],[4,5]],[[1,2],[0,1],[3,4]]]],[[[[1,2],[0,1],[1,4]]]]]]],[[[[[[[0,2],[1,2],[2,5]],[[0,3],[1,4],[1,2]],[[0,2],[1,4],[1,2]],[[0,2],[0,3],[1,2]],[[0,2],[0,3],[1,4]],[[3,5],[4,5],[2,5]],[[4,5],[0,3],[1,4]],[[3,5],[0,3],[1,4]],[[3,5],[4,5],[1,4]],[[3,5],[4,5],[0,3]]]],[[[[0,2],[1,2],[2,5]],[[3,4],[3,5],[0,3]]]]],[[[[[0,2],[1,2],[2,5]],[[3,4],[4,5],[1,4]]]],[[[[0,2],[1,2],[2,5]]]]]],[[[[[[4,5],[0,3],[1,4]],[[3,5],[0,3],[1,4]],[[3,5],[4,5],[1,4]],[[3,5],[4,5],[0,3]]]],[[[[3,4],[3,5],[0,3]]]]],[[[[[3,4],[4,5],[1,4]]]],[[]]]]]]]
#For each 
for hyperPlaneFile in os.listdir(hyperplaneDirectory):
    print("Starting with "+hyperPlaneFile)
    
    hyperplanes = open(hyperplaneDirectory+'/'+hyperPlaneFile, 'r').readlines()

    hyperPlanePath = finalSTLs+"/"+hyperPlaneFile 
    if not os.path.exists(hyperPlanePath):
        os.makedirs(hyperPlanePath)

    #print("Getting hypervectors")

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

    for spl4Path in os.listdir(spl4Directory):

            # Creates a list of the needed spl4 data of the form:
            # prisms[i][0-5][0-4]
            #        ^    ^   ^
            #        |    |   x,y,z,w
            #        |    vertex
            #        prism

            print("Starting with "+spl4Path)
            
            spl4 = open(spl4Directory+'/'+spl4Path, 'r').readlines()

            #print(len(spl4))

            i=0
            prisms=[None]*int((len(spl4)/7))
            print(str(len(spl4)/7)+" prisms to consider.")
            while(i<len(spl4)/7):
                #print("Prism "+str(i)+" beginning with comment line "+str(spl4[7*i]+str(i))+"\n")
                prism=[None]*6
                j=1
                while(j<7):
                    vertex=[float(spl4[j+(7*i)].split()[1]),float(spl4[j+(7*i)].split()[2]),float(spl4[j+(7*i)].split()[3]),float(spl4[j+(7*i)].split()[4])]
                    #print(vertex)
                    prism[j-1]=vertex
                    j=j+1
                #print("\nPrism")
                #print(prism)
                prisms[i]=prism
                i=i+1

            ##########CONFIRMED WORKING###########

            vertices=[0,1,2,3,4,5]
            constants=[]
            #if (argv[0] == '0'):
            #    constants.append(singleConstant)


            
            


            i=0
            #normalizer=(math.sqrt((a**2)+(b**2)+(c**2)+(d**2)))
            furthPosAny=None
            furthNegAny=None
            allPrismsDistanceInfo=[]
            while(i<len(prisms)):
                #print("Prism "+str(i))
                storePrism=[]
                furthPosPrism=None
                furthNegPrism=None
                for vertex in vertices:
                    #print("Checking the value of e required from the hyperplane to intersect vertex "+str(vertex))
                    #print(str(prisms[i][vertex]))
                    pX=prisms[i][vertex][0]
                    pY=prisms[i][vertex][1]
                    pZ=prisms[i][vertex][2]
                    pW=prisms[i][vertex][3]
                    #print("Sanity Check")
                    #print(a)
                    #print(b)
                    #print(c)
                    #print(d)
                    #print(pX)
                    #print(pY)
                    #print(pZ)
                    #print(pW)
                    eRequiredToHit=((a*pX)+(b*pY)+(c*pZ)+(d*pW))*(-1)
                    # e required to reach this distance is dis*normalizer, so we can remove this part
                    #print(eRequiredToHit)
                    storePrism.append(eRequiredToHit)
                    if (furthPosPrism==None):
                        #print("First furthest pos e")
                        furthPosPrism=eRequiredToHit
                    elif (eRequiredToHit>furthPosPrism):
                        #print("New furthest pos e")
                        furthPosPrism=eRequiredToHit
                    if (furthNegPrism==None):
                        #print("First furthest neg e")
                        furthNegPrism=eRequiredToHit
                    elif (eRequiredToHit<furthNegPrism):
                        #print("New furthest neg e")
                        furthNegPrism=eRequiredToHit
                #print("Appending this prism to the list")
                allPrismsDistanceInfo.append([furthPosPrism,furthNegPrism,[storePrism]])

                #print("\nFinal Checks\n")
                if (furthPosAny==None):
                    #print("First abs furthest pos e")
                    furthPosAny=furthPosPrism
                elif (furthPosPrism>furthPosAny):
                    #print("New abs furthest pos e")
                    furthPosAny=furthPosPrism
                if (furthNegAny==None):
                    #print("First abs furthest neg e")
                    furthNegAny=furthNegPrism
                elif (furthNegPrism<furthNegAny):
                    #print("New abs furthest neg e")
                    furthNegAny=furthNegPrism

                i+=1

            
            allPrismsDistanceInfo=[allPrismsDistanceInfo]
            allPrismsDistanceInfo.insert(0,(furthNegAny))
            allPrismsDistanceInfo.insert(0,(furthPosAny))
            #print("everything here "+str(allPrismsDistanceInfo))


            increment=((allPrismsDistanceInfo[1]-allPrismsDistanceInfo[0])/frames)
            print("\n increment to seperate frames "+str(increment)+"\n")


            i=0
            while (i<frames):
                constantValue=((i*increment)+0.5*increment)+allPrismsDistanceInfo[0]
                print("\nConstant to take cross-section "+str(constantValue)+" for frame "+str(i))
                frameAsSTL = open(hyperPlanePath+'/'+spl4Path[:-5]+str(i)+'.stl', 'w+')
                frameAsSTL.write("solid Created by DanJ being cool\n")
                collisionCount=0
                j=0
                while(j<len(prisms)):
                    #print("--")
                    prism=allPrismsDistanceInfo[2][j]
                    if (prism[0]>constantValue):
                        if (prism[1]<constantValue):
                            #print("YES")
                            #frameAsSTL.write("Starting Prism Notes\n")
                            aAbove=((prism[2][0][0]-constantValue)>0)
                            bAbove=((prism[2][0][1]-constantValue)>0)
                            cAbove=((prism[2][0][2]-constantValue)>0)
                            dAbove=((prism[2][0][3]-constantValue)>0)
                            eAbove=((prism[2][0][4]-constantValue)>0)
                            fAbove=((prism[2][0][5]-constantValue)>0)

                            #frameAsSTL.write(str(aAbove)+"\n")
                            #frameAsSTL.write(str(bAbove)+"\n")
                            #frameAsSTL.write(str(cAbove)+"\n")
                            #frameAsSTL.write(str(dAbove)+"\n")
                            #frameAsSTL.write(str(eAbove)+"\n")
                            #frameAsSTL.write(str(fAbove)+"\n")

                            if(not fAbove):
                                aAbove=not aAbove
                                bAbove=not bAbove
                                cAbove=not cAbove
                                dAbove=not dAbove
                                eAbove=not eAbove



                            #frameAsSTL.write(("\n"))
                            #frameAsSTL.write(str(intersectTriangleTable[aAbove][bAbove][cAbove][dAbove][eAbove])+"\n")

                            trianglesToRender=intersectTriangleTable[aAbove][bAbove][cAbove][dAbove][eAbove]

                            for polygon in trianglesToRender:
                                frameAsSTL.write("Polygon")
                                for triangle in polygon:
                                    frameAsSTL.write("facet normal\n")
                                    frameAsSTL.write("outer loop\n")
                                    #print(str(triangle))
                                    #print(str(prism))
                                    #print("\n")
                                    #print(str(constantValue))
                                    #print("\n")
                                    #print(str(prism[2][0][triangle[0][0]]))
                                    #print(str(prism[2][0][triangle[0][1]]))
                                    #print(str(prisms[j]))

                                    for vertex in triangle:
                                        #print("\nVertex of triangle sites between")
                                        #print(str(vertex))
                                        #print("Point 1 coords and distance to hyperplane")
                                        #print(str(prisms[j][vertex[0]]))
                                        #print(str(prism[2][0][triangle[0][0]]-constantValue))
                                        #print("Point 2 coords and distance to hyperplane")
                                        #print(str(prisms[j][vertex[1]]))
                                        #print(str(prism[2][0][triangle[0][1]]-constantValue))
                                        #print("Point that intersect hyperplane")

                                        #print("Coords for the first point")
                                        point1x = prisms[j][vertex[0]][0]
                                        #print(str(point1x))
                                        point1y = prisms[j][vertex[0]][1]
                                        #print(str(point1y))
                                        point1z = prisms[j][vertex[0]][2]
                                        #print(str(point1z))
                                        point1w = prisms[j][vertex[0]][3]
                                        #print(str(point1w))
                                        #print("Coords for the second point")
                                        point2x = prisms[j][vertex[1]][0]
                                        #print(str(point2x))
                                        point2y = prisms[j][vertex[1]][1]
                                        #print(str(point2y))
                                        point2z = prisms[j][vertex[1]][2]
                                        #print(str(point2z))
                                        point2w = prisms[j][vertex[1]][3]
                                        #print(str(point2w))


                                        #print("Constant (e)")
                                        #print(str(constantValue))
                                       
                                        if(point2x==point1x):
                                            Colx=point1x
                                        else:
                                            Colx=(((d*((point1x*(point2w-point1w))/(point2x-point1x)))-(d*point1w)+(b*((point1x*(point2y-point1y))/(point2x-point1x)))-(b*point1y)+(c*((point1x*(point2z-point1z))/(point2x-point1x)))-(c*point1z)-constantValue)/((a)+(b*((point2y-point1y)/(point2x-point1x)))+(c*((point2z-point1z)/(point2x-point1x)))+(d*((point2w-point1w)/(point2x-point1x)))))
                                        if(point2y==point1y):
                                            Coly=point1y
                                        else:
                                            Coly=(((a*((point1y*(point2x-point1x))/(point2y-point1y)))-(a*point1x)+(c*((point1y*(point2z-point1z))/(point2y-point1y)))-(c*point1z)+(d*((point1y*(point2w-point1w))/(point2y-point1y)))-(d*point1w)-constantValue)/((b)+(c*((point2z-point1z)/(point2y-point1y)))+(d*((point2w-point1w)/(point2y-point1y)))+(a*((point2x-point1x)/(point2y-point1y)))))
                                        if(point2z==point1z):
                                            Colz=point1z
                                        else:
                                            Colz=(((b*((point1z*(point2y-point1y))/(point2z-point1z)))-(b*point1y)+(d*((point1z*(point2w-point1w))/(point2z-point1z)))-(d*point1w)+(a*((point1z*(point2x-point1x))/(point2z-point1z)))-(a*point1x)-constantValue)/((c)+(d*((point2w-point1w)/(point2z-point1z)))+(a*((point2x-point1x)/(point2z-point1z)))+(b*((point2y-point1y)/(point2z-point1z)))))
                                        if(point2w==point1w):
                                            Colw=point1w
                                        else:
                                            Colw=(((c*((point1w*(point2z-point1z))/(point2w-point1w)))-(c*point1z)+(a*((point1w*(point2x-point1x))/(point2w-point1w)))-(a*point1x)+(b*((point1w*(point2y-point1y))/(point2w-point1w)))-(b*point1y)-constantValue)/((d)+(a*((point2x-point1x)/(point2w-point1w)))+(b*((point2y-point1y)/(point2w-point1w)))+(c*((point2z-point1z)/(point2w-point1w)))))

                                        #print("Final coords of collision point")
                                        #print(str(Colx))
                                        #print(str(Coly))
                                        #print(str(Colz))
                                        #print(str(Colw))

                                        #print("Checking the split")
                                        #if(point2x==point1x):
                                        #    print("Perfect match")
                                        #else:
                                        #    print((point2x-Colx)/(Colx-point1x))
                                        #if(point2y==point1y):
                                        #    print("Perfect match")
                                        #else:
                                        #    print((point2y-Coly)/(Coly-point1y))
                                        #if(point2z==point1z):
                                        #    print("Perfect match")
                                        #else:
                                        #    print((point2z-Colz)/(Colz-point1z))
                                        #if(point2w==point1w):
                                        #    print("Perfect match")
                                        #else:
                                        #    print((point2w-Colw)/(Colw-point1w))


                                        #print("Converting the 4 dimensional coords of Cx,Cy,Cz,Cw into 3 dimensional fX,fY,fZ")


                                        fX=((Ax*Colx)+(Bx*Coly)+(Cx*Colz)+(Dx*Colw)/(math.sqrt((Ax**2)+(Bx**2)+(Cx**2)+(Dx**2))))
                                        fY=((Ay*Colx)+(By*Coly)+(Cy*Colz)+(Dy*Colw)/(math.sqrt((Ay**2)+(By**2)+(Cy**2)+(Dy**2))))
                                        fZ=((Az*Colx)+(Bz*Coly)+(Cz*Colz)+(Dz*Colw)/(math.sqrt((Az**2)+(Bz**2)+(Cz**2)+(Dz**2))))

                                        collisionCount=collisionCount+1
                                        #print(str(fX)+str(fY)+str(fZ))
                                        #print(fX)
                                        #print(fY)
                                        #print(fZ)
                                        frameAsSTL.write("vertex "+str(fX)+" "+str(fY)+" "+str(fZ)+"\n")





                                        #CHECK THE RESPONSE TIMES FOR THE BELOW TWO METHODS
                                        #For each point which intersects the plane Xn,Yn,Zn,Wn, get the final coordinates for it compared to the plane itself. xf.yf,zf
                                        #
                                        #xf=AxXn+BxYn+CxZn+DxWn/(sqrt(AxAx+BxBx+CxCx+DxDx))
                                        #
                                        #xf=Xn+Zn((-a-d)/c)+Wn/(sqrt(2+((-a-d)(-a-d)/cc)))
                                        #
                                        #yf=AyXn+ByYn+CyZn+DyWn/(sqrt(AyAy+ByBy+CyCy+DyDy))
                                        #
                                        #yf=-abXn+Yn(aa+cc+dd)-cbZn-dbWn/((-ab)(-ab)+(aa+cc+dd)(aa+bb+cc)+(-cb)(-cb)+(-db)(-db))
                                        #
                                        #zf=AzXn+BzYn+CzZn+DzWn/(sqrt(AzAz+BzBz+CzCz+DzDz))
                                        #
                                        #zf=Xn+Zn((c(d-a))/(d(a+d)+cc))+Wn((ad-aa+cc)/(d(a+d)+cc))
                                    frameAsSTL.write("endloop\n")
                                    frameAsSTL.write("endfacet\n")  
                    j=j+1
                print("Number of prisms intersected by this frame is "+str(collisionCount))
                i+=1

            