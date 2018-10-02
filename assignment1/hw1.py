#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np
import math

def histogram_times(filename):
    newlist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    counter = 0
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if counter != 0:
                try:
                    if row[1][0:1] == "0":
                        hour = row[1][1:2]
                    else:
                        hour = row[1][0:2]
                    hour = int(hour)
                    newlist[hour] = newlist[hour] + 1
                except ValueError:
                    pass
            counter += 1
    return newlist




def weigh_pokemons(filename, weight):
    newlist = list()
    jsonResponse=json.loads(open(filename).read())
    for item in jsonResponse["pokemon"]:
        name = item["name"]
        weightCheck = item["weight"]
        weightCheck = weightCheck.replace("kg", "")
        weightCheck1 = float(weightCheck)
        if weightCheck1 == weight:
            newlist.append(name)
    return newlist



def single_type_candy_count(filename):
    totalCandies = 0
    jsonResponse = json.loads(open(filename).read())
    for item in jsonResponse["pokemon"]:
        try:
            amount = item["candy_count"]
            totalCandies += amount
        except KeyError:
            totalCandies += 0
    return totalCandies






def reflections_and_projections(points):
    newPoints1 = np.flip(points, (0, 1))

    rotation = [[0,-1],[1,0]]
    newPoints2 = np.matmul(rotation,newPoints1)

    project = [[0.1,0.3],[0.3,0.9]]
    newPoints3 = np.matmul((project,newPoints2))

    return newPoints3






def normalize(image):
    maxInt = np.amax(image)
    minInt = np.amin(image)
    newList = ((255)/(maxInt-minInt) * (image - minInt))
    return newList





def sigmoid_normalize(image):
    maxInt = np.amax(image)
    alist = [i / maxInt for i in image]
    alist = [1 / (1 + math.exp(-i)) for i in image]



print(weigh_pokemons("pokedex.json",10.0))
print(single_type_candy_count("pokedex.json"))
print(histogram_times("airplane_crashes.csv"))
