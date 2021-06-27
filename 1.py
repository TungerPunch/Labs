import math 

h=1585
V=41
g=1.62
M=2150
u=3660
a_max=29.43
m=200
alfa=1
r=0
dt=0.1
t=0
M=M+m
a=0
while(h-(V**2)/(a_max-g)>0 and m>0):
    print(V,'  ',h,'  ',alfa,'  ',r*dt,'  ',t,'  ',m)
    a=0
    r=M*a/u
    h=h-(V*dt-(a-g)*(dt**2)/2)
    V=V+(g-a)*dt
    M=M-r*dt
    t=t+dt
    m=m-r*dt

    
while(h>0 and m>0 and V>3):
    print(V,'  ',h,'  ',alfa,'  ',r*dt,'  ',t)
    a=a_max
    r=M*a/u
    h=h-(V*dt-(a-g)*(dt**2)/2)
    V=V+(g-a)*dt
    M=M-r*dt
    t=t+dt
    m=m-r*dt

while(h>0 and m>0):
    print(V,'  ',h,'  ',alfa,'  ',r*dt,'  ',t)
    a=g
    r=M*a/u
    h=h-(V*dt-(a-g)*(dt**2)/2)
    V=V+(g-a)*dt
    M=M-r*dt
    t=t+dt
    m=m-r*dt


print(V,'  ',0,'  ',alfa,'  ',r*dt,'  ',t)



