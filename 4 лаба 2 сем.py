import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def vp(p, p1, p2): #по точкам
    return (p1[0]-p[0])*(p2[1]-p[1])-(p1[1]-p[1])*(p2[0]-p[0])

def sp(p1, p2): #по векторам
    return p1[0]*p2[0]+p1[1]*p2[1]

def dist_2(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def next_point(cur_point, prev_point, points):

    result = None

    for now in points:
        if now == cur_point or now == prev_point:
            continue

        if vp(prev_point, cur_point, now)==0:
            if sp(sub(cur_point,prev_point), sub(now, prev_point))>0 and (result==None or result!=None and dist_2(cur_point, result)<dist_2(cur_point, now)) and dist_2(prev_point,now)>dist_2(prev_point,cur_point):
                result=now
            continue

        if result == None:
            result=now
            continue

        if vp(cur_point, now, result) > 0 or vp(cur_point, now, result)==0 and dist_2(cur_point, result)<dist_2(cur_point, now):
                                                                                                             result=now
    return result

def sub(p1, p2):
    return [p1[0]-p2[0], p1[1]-p2[1]]

a = pd.read_csv('convex.csv', header=None)
variant=10  -1

points=[]

i=0
while i<1000:
    points.append([a.loc[variant, i], a.loc[variant, i+1]])
    i+=2


newX=[]
newY=[]


point = points[0]

for i in range(1, len(points)):
    if points[i][1]<point[1] or points[i][1]==point[1] and points[i][0]<point[0]:
        point=points[i]

new_points=[point]

point=next_point(point, [point[0]-1, point[1]], points)


while point!=new_points[0]:
    new_points.append(point)

    point=next_point(point, new_points[len(new_points)-2], points)

new_points.append(new_points[0])

i=0
while i<len(new_points):
    newX.append(new_points[i][0])
    newY.append(new_points[i][1])
    i+=1
newX.append(newX[0])
newY.append(newY[0])
plt.plot(newX, newY, color="red")

i=0
X=[]
Y=[]

while i<1000:
    X.append(a.loc[variant, i])
    Y.append(a.loc[variant, i+1])
    i+=2

plt.scatter(X, Y)

plt.scatter([newX[0]], [newY[0]], color="red")

pd.DataFrame({'x':newX, 'y':newY}).to_csv('new.csv')