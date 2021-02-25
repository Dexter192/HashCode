import pandas as pd
import os
import numpy as np

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
