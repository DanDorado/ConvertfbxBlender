import math

#Given:
# point A (point1x,point1y,point1z,point1w)  26
# point B (point2x,point2y,point2z,point2w)
# plane ax+by+cz+dw+e=0

# 2

#Find the point where they collide (Cx,Cy,Cz,Cw)
point1x=2
point1y=3
point1z=4
point1w=5

point2x=3
point2y=2
point2z=1
point2w=8

a=3
b=6
c=3
d=8
e=1

#3


#We Know
VectorAB=[(point2x-point1x),(point2y-point1y),(point2z-point1z),(point2w-point1w)]


# 4

#WE DON't KNOW n

Cx=point1x+n(point2x-point1x)
Cy=point1y+n(point2y-point1y)
Cz=point1z+n(point2z-point1z)
Cw=point1w+n(point2w-point1w)

# 6

#Substituting into the plane

a(point1x+n(point2x-point1x))+b(point1y+n(point2y-point1y))+c(point1z+n(point2z-point1z))+d(point1w+n(point2w-point1w))+e=0

(a*point1x)+n(a*(point2x-point1x))+(b*point1y)+n(b*(point2y-point1y))+(c*point1z)+n(c*(point2z-point1z))+(d*point1w)+n(d*(point2w-point1w))+e=o

n(a*(point2x-point1x))+n(b*(point2y-point1y))+n(c*(point2z-point1z))+n(d*(point2w-point1w))=-(a*point1x)-(b*point1y)-(c*point1z)-(d*point1w)-e

n((a*(point2x-point1x))+(b*(point2y-point1y))+(c*(point2z-point1z))+(d*(point2w-point1w)))=-(a*point1x)-(b*point1y)-(c*point1z)-(d*point1w)-e

n = (-(a*point1x)-(b*point1y)-(c*point1z)-(d*point1w)-e)/((a*(point2x-point1x))+(b*(point2y-point1y))+(c*(point2z-point1z))+(d*(point2w-point1w)))

# 16



#Finalize

Cx = point1x+((n)*(point2x-point1x))
Cy = point1y+((n)*(point2y-point1y))
Cz = point1z+((n)*(point2z-point1z))
Cw = point1w+((n)*(point2w-point1w))


# 26 25 25