import pandas as pd
import os
import numpy as np

class simulation:
    def __init__(duration, num_intersections, total_streets, total_cars, bonus_points):
        self.duration = duration
        self.total_intersections = total_intersections
        self.total_streets = total_streets
        self.total_cars = total_cars
        self.bonus_points = bonus_points

class car:
    def __init__(self, num_streets, route):
        self.num_streets = num_streets
        self.route = route
        self.current_street = route[0]
        #Gets the current position in the current street
        self.current_position = route[0].travel_time

class street:
    def __init__(self,start,end,name,travel_time):
        self.start = start
        self.end = end
        self.name = name
        self.travel_time = travel_time


class intersection:
    def __init__(self, id, number_streets, streets):
        self.number_streets = number_streets
        self.streets = streets
        self.green = np.zeros(len(simulation.duration))
        self.id = id
        #List of tuples (routename, seconds green)
        self.cycle = []#[(routename, 2), (routename2, 3), (routename3, 1)]



def load_file(name):
    with open('input/'+name) as infile:
        return [line.strip() for line in infile.readlines()]
    return lines

def clean_file(the_file):
    splitted = [file.split(' ') for file in the_file]
    splitted = [[int(x) for x in list] for list in splitted]
    return splitted

def flat_list(cleaned_file):
    flattened_list = []
    for sublist in cleaned_file:
        for item in sublist:
            flattened_list.append(int(item))
    return flattened_list

def load_files():
    names = os.listdir("./input/")
    print(names)
    inputs = []
    for file_name in names:
        input = load_file(file_name)
        clean_input = clean_file(input)
        inputs.append(clean_input)
    return inputs

input = load_files()
print(input)
