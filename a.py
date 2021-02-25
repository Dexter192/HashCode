from hashcode_parser import *
from pprint import pprint


for name in ["a","b","c","d","e","f"]:
    #ALGORITHM 2 - Prioritize streets with heavy traffic
    simulation_info, cars, streets = load_file(name+'.txt')


    it = 0
    intersections = dict()
    for it in range(0,simulation_info.total_intersections):
        intersection = Intersection(it)
        intersections[it] = intersection
        it += 1


    streets_count = {}
    for car in cars:
        #print(car.num_streets)
        for street in car.route:
            if street not in streets_count:
                streets_count[street] = 1
            else:
                streets_count[street] += 1

    for street in streets:
        if street.name not in streets_count:
            streets_count[street.name] = 0
        else:
            streets_count[street.name] = 1
            intersections[street.end].add_street_with_weight(street.name, streets_count[street.name])
        # pprint(vars(intersections[street.end]))

    for intersection in intersections.values():
        for i, street in enumerate(intersection.streets):
            if intersection.weights[i] > 0:
                intersection.cycle.append((street, intersection.weights[i]))

    intersections = [x for x in intersections.values() if x.cycle != []]
    #for intersection in intersections:
        #print(intersection.cycle)

    write_output(name+'.out', intersections)


"""
for name in ["a","b","c","d","e","f"]:
    simulation_info, cars, streets = load_file(name+'.txt')

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
    # for intersection in intersections.values():
    #     intersection.cycle = [(s.name ,1) for s in intersection.streets]


    write_output(name+'.out', intersections.values())
"""
