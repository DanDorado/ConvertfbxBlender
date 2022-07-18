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

ax+by+cz+dw+e=0

(a*Cx)+(b*Cy)+(c*Cz)+(d*Cw)+e=0


(Cx-point1x)/(point2x-point1x)
=
(Cy-point1y)/(point2y-point1y)
=
(Cz-point1z)/(point2z-point1z)
=
(Cw-point1w)/(point2w-point1w)

(Cx-point1x)/(point2x-point1x)
=
(Cy-point1y)/(point2y-point1y)

((Cx-point1x)*(point2y-point1y))/(point2x-point1x)=(Cy-point1y)

Cy=(point1y+(((Cx-point1x)*(point2y-point1y))/(point2x-point1x)))
Cz=(point1z+(((Cx-point1x)*(point2z-point1z))/(point2x-point1x)))
Cw=(point1w+(((Cx-point1x)*(point2w-point1w))/(point2x-point1x)))

(a*Cx)+(b*(point1y+(((Cx-point1x)*(point2y-point1y))/(point2x-point1x))))+(c*(point1z+(((Cx-point1x)*(point2z-point1z))/(point2x-point1x))))+(d*(point1w+(((Cx-point1x)*(point2w-point1w))/(point2x-point1x))))+e=0


(a*Cx)+
(swapb)+
(c*(point1z+(((Cx-point1x)*(point2z-point1z))/(point2x-point1x))))+
(d*(point1w+(((Cx-point1x)*(point2w-point1w))/(point2x-point1x))))+
e=0

swap1=Cx(point2y-point1y)-point1x(point2y-point1y)

swap2=(swap1)/(point2x-point1x)

swap2=Cx((point2y-point1y)/(point2x-point1x))-((point1x(point2y-point1y))/(point2x-point1x))

swap3=(point1y+(swap2))

swap3=Cx((point2y-point1y)/(point2x-point1x))-((point1x(point2y-point1y))/(point2x-point1x))+point1y

swapb=(b*swap3)

swapb=Cx(b((point2y-point1y)/(point2x-point1x)))-(b((point1x(point2y-point1y))/(point2x-point1x)))+(b*point1y)
swapc=Cx(c((point2z-point1z)/(point2x-point1x)))-(c((point1x(point2z-point1z))/(point2x-point1x)))+(c*point1z)
swapd=Cx(d((point2w-point1w)/(point2x-point1x)))-(d((point1x(point2w-point1w))/(point2x-point1x)))+(d*point1w)


AllBackIn

Cx(a)+
(Cx(b((point2y-point1y)/(point2x-point1x)))-(b((point1x(point2y-point1y))/(point2x-point1x)))+(b*point1y))+
(Cx(c((point2z-point1z)/(point2x-point1x)))-(c((point1x(point2z-point1z))/(point2x-point1x)))+(c*point1z))+
(Cx(d((point2w-point1w)/(point2x-point1x)))-(d((point1x(point2w-point1w))/(point2x-point1x)))+(d*point1w))+
e=0


Cx(a)+
Cx(b((point2y-point1y)/(point2x-point1x)))
-(b((point1x(point2y-point1y))/(point2x-point1x)))
+(b*point1y)
+Cx(c((point2z-point1z)/(point2x-point1x)))
-(c((point1x(point2z-point1z))/(point2x-point1x)))
+(c*point1z)
+Cx(d((point2w-point1w)/(point2x-point1x)))
-(d((point1x(point2w-point1w))/(point2x-point1x)))
+(d*point1w)
+e=0




Cx(a)+
Cx(b((point2y-point1y)/(point2x-point1x)))
+Cx(c((point2z-point1z)/(point2x-point1x)))
+Cx(d((point2w-point1w)/(point2x-point1x)))
-(d((point1x(point2w-point1w))/(point2x-point1x)))
+(d*point1w)
-(b((point1x(point2y-point1y))/(point2x-point1x)))
+(b*point1y)
-(c((point1x(point2z-point1z))/(point2x-point1x)))
+(c*point1z)
+e
=0


Cx(a)+
Cx(b((point2y-point1y)/(point2x-point1x)))
+Cx(c((point2z-point1z)/(point2x-point1x)))
+Cx(d((point2w-point1w)/(point2x-point1x)))
=
(d((point1x(point2w-point1w))/(point2x-point1x)))-(d*point1w)+(b((point1x(point2y-point1y))/(point2x-point1x)))-(b*point1y)+(c((point1x(point2z-point1z))/(point2x-point1x)))-(c*point1z)-e



Cx((a)+(b((point2y-point1y)/(point2x-point1x)))+(c((point2z-point1z)/(point2x-point1x)))+(d((point2w-point1w)/(point2x-point1x))))
=
(d((point1x(point2w-point1w))/(point2x-point1x)))-(d*point1w)+(b((point1x(point2y-point1y))/(point2x-point1x)))-(b*point1y)+(c((point1x(point2z-point1z))/(point2x-point1x)))-(c*point1z)-e


Cx=(((d((point1x(point2w-point1w))/(point2x-point1x)))-(d*point1w)+(b((point1x(point2y-point1y))/(point2x-point1x)))-(b*point1y)+(c((point1x(point2z-point1z))/(point2x-point1x)))-(c*point1z)-e)/((a)+(b((point2y-point1y)/(point2x-point1x)))+(c((point2z-point1z)/(point2x-point1x)))+(d((point2w-point1w)/(point2x-point1x)))))
Cy=(((a((point1y(point2x-point1x))/(point2y-point1y)))-(a*point1x)+(c((point1y(point2z-point1z))/(point2y-point1y)))-(c*point1z)+(d((point1y(point2w-point1w))/(point2y-point1y)))-(d*point1w)-e)/((b)+(c((point2z-point1z)/(point2y-point1y)))+(d((point2w-point1w)/(point2y-point1y)))+(a((point2x-point1x)/(point2y-point1y)))))
Cz=(((b((point1z(point2y-point1y))/(point2z-point1z)))-(b*point1y)+(d((point1z(point2w-point1w))/(point2z-point1z)))-(d*point1w)+(a((point1z(point2x-point1x))/(point2z-point1z)))-(a*point1x)-e)/((c)+(d((point2w-point1w)/(point2z-point1z)))+(a((point2x-point1x)/(point2z-point1z)))+(b((point2y-point1y)/(point2z-point1z)))))
Cw=(((c((point1w(point2z-point1z))/(point2w-point1w)))-(c*point1z)+(a((point1w(point2x-point1x))/(point2w-point1w)))-(a*point1x)+(b((point1w(point2y-point1y))/(point2w-point1w)))-(b*point1y)-e)/((d)+(a((point2x-point1x)/(point2w-point1w)))+(b((point2y-point1y)/(point2w-point1w)))+(c((point2z-point1z)/(point2w-point1w)))))
