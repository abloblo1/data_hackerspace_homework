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
        if len(item["type"]) == 1:
            try:
                amount = item["candy_count"]
                totalCandies += amount
            except KeyError:
                totalCandies += 0
    return totalCandies


def reflections_and_projections(points):
    flip = [[1,0],[0,-1]]
    newPoints1 = np.matmul(flip,points)
    for i in range(len(newPoints1[1])):
        newPoints1[1][i] += 1

    rotation = np.matrix([[math.cos(math.pi/2), -math.sin(math.pi/2)], [math.sin(math.pi/2), math.cos(math.pi/2)]])
    newPoints2 = np.matmul(rotation, newPoints1)

    projection = np.matrix([[1, 3], [3, 3**2]])/(3**2 + 1)
    newPoints3 = np.matmul(projection, newPoints2)
    return newPoints3



def normalize(image):
    maxInt = np.amax(image)
    minInt = np.amin(image)
    newList = (255.0/(maxInt-minInt)) * (image - minInt)
    return newList


def sigmoid_normalize(image, a):
    for i in range(len(image)):
        for j in range(len(image[i])):
            image[i][j] = int(round(( 255.0 * (( (1 + (math.e**( -(1.0/a)*(image[i][j] - 128) )) ) )**-1))))
    return image



print("\n")
print(weigh_pokemons("pokedex.json",10.0))
print(single_type_candy_count("pokedex.json"))
print(histogram_times("airplane_crashes.csv"))
print(reflections_and_projections([[3,5],[8,2]]))
image = np.array([[60, 70, 90, 100],
                  [80, 90, 55, 120],
                  [205, 122, 87, 90],
                  [103, 145, 140, 104]])
print("asdfasdf",normalize(image))
print(sigmoid_normalize(image, 100))
