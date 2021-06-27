import math 
import matplotlib.pyplot as plt
import numpy as np

Y=0
X=0
Vx=0
Vy=0
V=0
g=1.62
M=2150
u=3660
a_max=29.43
pi=3.1416
m=1000
alfa=0
r=0
dt=0.1
t=0
M=M+m
a=0

K=[]
L=[]
I=[]
O=[]
U=[]
fig = plt.figure()
fig = plt.figure()

while(m>520):
    print(Vx,'  ',Vy,'  ',X,'  ',Y,'  ',alfa,'  ',r*dt,'  ',t,)
    
    V=math.pow(math.pow(Vx, 2)+math.pow(Vy, 2), 0.5)
    
    K.append(t)
    L.append(V)
    I.append(X)
    O.append(Y)
    U.append(a)
    a=a_max
    
    ap=math.pow((math.pow(a, 2)+math.pow(g, 2)-2*a*g*math.cos(3*pi/4)), 0.5)
    
    alfa=math.acos(((math.pow(ap, 2)+math.pow(g, 2)-math.pow(a, 2))/(2*ap*g)))
    alfa=math.degrees(alfa)
    r=M*ap/u
    V=a*t
    Vy=V/(math.pow(2, 0.5))
    Vx=V/(math.pow(2, 0.5))
    VY=-Vy
    
    X=X+Vx*dt+a*math.pow(dt, 2)/(math.pow(2, 0.5)*2)
    Y=Y+Vy*dt+a*math.pow(dt, 2)/(math.pow(2, 0.5)*2)
    
    M=M-r*dt
    t=t+dt
    m=m-r*dt
    math.degrees(alfa)

alfa=45
   
while(Vy>0):
    print(Vx,'  ',Vy,'  ',X,'  ',Y,'  ',alfa,'  ',r*dt,'  ',t,)
    
    V=math.pow(math.pow(Vx, 2)+math.pow(Vy, 2), 0.5)
    
    K.append(t)
    L.append(V)
    I.append(X)
    O.append(Y)
    U.append(a)
    a=g
    r=0
    Vy=Vy-g*dt
    Y=Y+Vy*dt-g*math.pow(dt, 2)/2
    X=X+Vx*dt
    alfa=math.atan(Vy/Vx)
    alfa=90-math.degrees(alfa)
    
    M=M-r*dt
    t=t+dt
    m=m-r*dt



while(m>420):
    print(Vx,'  ',Vy,'  ',X,'  ',Y,'  ',alfa,'  ',r*dt,'  ',t,)
    
    V=math.pow(math.pow(Vx, 2)+math.pow(Vy, 2), 0.5)
    
    K.append(t)
    L.append(V)
    I.append(X)
    O.append(Y)
    U.append(a)
    a=0
    alpha=0
    r=M*g/u
    
    X=X+Vx*dt
    Y=Y+Vy*dt
    
    M=M-r*dt
    t=t+dt
    m=m-r*dt
   
while(X<246025):
    print(Vx,'  ',Vy,'  ',X,'  ',Y,'  ',alfa,'  ',r*dt,'  ',t,)
    
    V=math.pow(math.pow(Vx, 2)+math.pow(Vy, 2), 0.5)
    
    K.append(t)
    L.append(V)
    I.append(X)
    O.append(Y)
    U.append(a)
    a=g
    r=0
    Vy=Vy-g*dt
    Y=Y+Vy*dt-g*math.pow(dt, 2)/2
    X=X+Vx*dt
    alfa=math.atan(Vy/Vx)
    alfa=90-math.degrees(alfa)
    
    M=M-r*dt
    t=t+dt
    m=m-r*dt
    

V=math.pow(math.pow(Vx, 2)+math.pow(Vy, 2), 0.5)
T=0
alfa=-90
while(X<250000 and Y>-1 and alfa<=0 and Vx>0):
    print(Vx,'  ',Vy,'  ',X,'  ',Y,'  ',alfa,'  ',r*dt,'  ',t,)
    
    K.append(t)
    L.append(V)
    I.append(X)
    O.append(Y)
    U.append(a)
    a=a_max
    
    ap=math.pow((math.pow(a, 2)+math.pow(g, 2)-2*a*g*(math.cos(math.asin(Vx/V)))), 0.5)
    alfa=math.acos(((math.pow(ap, 2)+math.pow(g, 2)-math.pow(a, 2))/(2*ap*g)))
    alfa=-(90-math.degrees(alfa))
    alfa=math.radians(alfa)
    V=V-a*dt
    r=M*ap/u
    ax=Vx/V*a
    ay=math.fabs(Vy/V)*a
    Vx=Vx-ax*dt
    Vy=Vy+ay*dt
    
    X=X+Vx*dt-ax*(math.pow(dt, 2))/2
    Y=Y+Vy*dt+ay*(math.pow(dt, 2))/2
    
    alfa=-math.degrees(alfa)
           
    M=M-r*dt
    t=t+dt
    m=m-r*dt

while(Vx>2):
    print(Vx,'  ',Vy,'  ',X,'  ',Y,'  ',alfa,'  ',r*dt,'  ',t,)
    
    V=math.pow(math.pow(Vx, 2)+math.pow(Vy, 2), 0.5)
    K.append(t)
    L.append(V)
    I.append(X)
    O.append(Y)
    U.append(a)
    
    alfa=90
    a=a_max
    r=M*a/u
    Vx=Vx-a*dt
    Vy=Vy-g*dt
    X=X+Vx*dt-a*math.pow(dt, 2)/2
    Y=Y+Vy*dt-g*math.pow(dt, 2)/2
    
    M=M-r*dt
    t=t+dt
    m=m-r*dt

while(Vx!=0):
    print(Vx,'  ',Vy,'  ',X,'  ',Y,'  ',alfa,'  ',r*dt,'  ',t,)
    
    V=math.pow(math.pow(Vx, 2)+math.pow(Vy, 2), 0.5)
    K.append(t)
    L.append(V)
    I.append(X)
    O.append(Y)
    U.append(a)
    
    alfa=90
    a=Vx/dt
    r=M*a/u
    Vx=Vx-a*dt
    Vy=Vy-g*dt
    X=X+Vx*dt-a*math.pow(dt, 2)/2
    Y=Y+Vy*dt-g*math.pow(dt, 2)/2
    
    M=M-r*dt
    t=t+dt
    m=m-r*dt
 
while(X<250001 and Y>40):
    print(Vx,'  ',Vy,'  ',X,'  ',Y,'  ',alfa,'  ',r*dt,'  ',t,)
    
    V=math.pow(math.pow(Vx, 2)+math.pow(Vy, 2), 0.5)
    K.append(t)
    L.append(V)
    I.append(X)
    O.append(Y)
    U.append(a)
    a=g
    r=0
    Vy=Vy-g*dt
    Y=Y+Vy*dt-g*math.pow(dt, 2)/2
    X=X+Vx*dt
    alfa=-180
    
    
    M=M-r*dt
    t=t+dt
    m=m-r*dt

while(X<250001 and Y>-1 and Vy<-1):
    print(Vx,'  ',Vy,'  ',X,'  ',Y,'  ',alfa,'  ',r*dt,'  ',t,)
    
    V=math.pow(math.pow(Vx, 2)+math.pow(Vy, 2), 0.5)
    K.append(t)
    L.append(V)
    I.append(X)
    O.append(Y)
    U.append(a)
    
    a=a_max
    r=M*a/u
    Vy=Vy+a*dt
    Y=Y+Vy*dt-a*math.pow(dt, 2)/2
    alfa=0
    
    M=M-r*dt
    t=t+dt
    m=m-r*dt
r=0

while(Y>-2):
    print(Vx,'  ',Vy,'  ',X,'  ',Y,'  ',alfa,'  ',r*dt,'  ',t,)
    
    V=math.pow(math.pow(Vx, 2)+math.pow(Vy, 2), 0.5)
    K.append(t)
    L.append(V)
    I.append(X)
    O.append(Y)
    U.append(a)
    a=g
    r=0
    Vy=Vy-g*dt
    Y=Y+Vy*dt-g*math.pow(dt, 2)/2
    X=X+Vx*dt
    alfa=0
    
    M=M-r*dt
    t=t+dt
    m=m-r*dt

V=math.pow(math.pow(Vx, 2)+math.pow(Vy, 2), 0.5)

K.append(t)
L.append(V)
I.append(X)
O.append(Y)
U.append(a)
alfa=0
a=-Vy/dt
r=M*a/u

Vy=Vy+a*dt-g*dt
Y=Y+Vy*dt-(a-g)*math.pow(dt, 2)/2
    
M=M-r*dt
t=t+dt
m=m-r*dt
while(Y>-1):
    print(Vx,'  ',Vy,'  ',X,'  ',Y,'  ',alfa,'  ',r*dt,'  ',t,)
    
    V=math.pow(math.pow(Vx, 2)+math.pow(Vy, 2), 0.5)
    K.append(t)
    L.append(V)
    I.append(X)
    O.append(Y)
    U.append(a)
    a=g
    r=0
    Vy=Vy-g*dt
    Y=Y+Vy*dt-g*math.pow(dt, 2)/2
    X=X+Vx*dt
    alfa=0
    
    M=M-r*dt
    t=t+dt
    m=m-r*dt
print(Vx,'  ',Vy,'  ',X,'  ',Y,'  ',alfa,'  ',r*dt,'  ',t,)

V=math.pow(math.pow(Vx, 2)+math.pow(Vy, 2), 0.5)

K.append(t)
L.append(V)
I.append(X)
O.append(Y)
U.append(a)

fig = plt.figure()
graf1=plt.plot(K, L)
plt.xlabel("t")
plt.ylabel("V")
plt.grid(True)


fig = plt.figure()
graf2=plt.plot(I, O)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

fig = plt.figure()
graf3=plt.plot(K, U)
plt.xlabel("t")
plt.ylabel("a")
plt.grid(True)
plt.show()
