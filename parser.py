import pandas as pd
import os
import numpy as np

class Simulation:
    def __init__(self, duration, total_intersections, total_streets, total_cars, bonus_points):
        self.duration = duration
        self.total_intersections = total_intersections
        self.total_streets = total_streets
        self.total_cars = total_cars
        self.bonus_points = bonus_points

class Car:
    def __init__(self, num_streets, route):
        self.num_streets = num_streets
        self.route = route
        #self.current_street = route[0]
        #Gets the current position in the current street
        #self.current_position = route[0].travel_time

class Street:
    def __init__(self, start,end,name,travel_time):
        self.start = start
        self.end = end
        self.name = name
        self.travel_time = travel_time


class Intersection:
    def __init__(self, id, number_streets, streets):
        self.number_streets = number_streets
        self.streets = streets
        self.green = np.zeros(len(simulation.duration))
        self.id = id
        #List of tuples (routename, seconds green)
        self.cycle = []#[(routename, 2), (routename2, 3), (routename3, 1)]



def load_file(name):
    with open('input/'+name) as infile:
        lines = [line.strip() for line in infile.readlines()]
    simulation_info = load_simulation_info(lines[0])
    streets = load_streets(lines[1:simulation_info.total_streets])
    cars = load_cars(lines[simulation_info.total_streets+1:-1])
    return simulation_info, cars, streets

def load_simulation_info(input_line):
    splitted = input_line.split(' ')
    splitted = [int(x) for x in splitted]
    return Simulation(splitted[0], splitted[1], splitted[2], splitted[3], splitted[4])


def load_cars(lines):
    list_cars=[]
    for line in lines:
        attributes = line.split(' ')
        car1 = Car(int(attributes[0]), attributes[1:-1])
        list_cars.append(car1)
    return list_cars


def load_streets(lines):
    list_streets = []
    for line in lines:
        splitted = line.split(' ')
        street = Street(int(splitted[0]),int(splitted[1]),splitted[2],int(splitted[3]))
        list_streets.append(street)
    return list_streets

simulation_info, cars, streets = load_file('a.txt')
print(simulation_info.duration)
print(cars[0].route[0])
print(streets[0].name)
