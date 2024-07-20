import random
import math

num_points=int(input("input point numbers:"))
points=[]
start_point=1.0
end_point=10.0

random_val = random.uniform(start_point, end_point)

for i in range(num_points):
    temp_points=(
        round(random.uniform(start_point, end_point),1),
        round(random.uniform(start_point, end_point),1)
        )
    points.append(temp_points)

def euclideanDistance(tuple1=(1,1),tuple2=(1,1)):
    distance=math.sqrt(((tuple1[0]-tuple2[0])**2)+((tuple1[1]-tuple2[1])**2))
    return round(distance,1)

print(f"'Points' list is: {points}\n")  

distances=[]

for i in range(len(points)-1):
    for j in range(i+1,len(points)):
        distances.append(round(euclideanDistance(points[i],points[j]),1))

print(f"'Distances' list is: {distances}\n")  

min_value=distances[0]
for i in range(len(distances)):
    if distances[i]<min_value:
        min_value=distances[i]

print(f"Minimum euclid distance in the list is: {min_value}\n")        
