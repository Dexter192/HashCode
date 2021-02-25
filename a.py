from hashcode_parser import *

simulation_info, cars, streets = load_file('a.txt')

it = 0
intersections = dict()
for it in range(0,simulation_info.total_intersections):
    intersection = Intersection(it)
    intersections[it] = intersection
    it += 1

#print(list(intersections.values()))
#{0 -> Intersection with id 0, 1 -> Intersection with id 1}
for street in streets:
    intersections[street.end].add_street(street)


#ALGORITHM 1 REALLY BAD
for intersection in intersections.values():
    intersection.cycle = [(s.name ,1) for s in intersection.streets]
    print(intersection.cycle)

write_output('a.out', intersections.values())
