import parser
from parser import *
simulation_info, cars, streets = load_file('a.txt')

it = 0
intersections = dict()
for it in range(0,simulation_info.total_intersections):
    intersection = Intersection(it)
    intersections[it] = intersection
    it += 1
#{0 -> Intersection with id 0, 1 -> Intersection with id 1}

print(intersections.items())
#for street in streets:
