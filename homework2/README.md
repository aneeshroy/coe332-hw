# Return of the JSON: Robots and Data Formats

## Overview

In this folder, the two scripts contain files that run a simulation of a robot collecting meteorite samples on Mars. 5 different meteorites are strewn in random locations and copied to a JSON file by the first script, generate_sites.py. The second script, calculate_trip.py, simulates a robot traveling to each meteorite site and taking a sample, with the script calculating the time for each and printing the info, as well as the total time after the trip is complete.

## Description

generate_sites.py is the first script, that randomly generates 5 meteorite locations within the latitudes (16.0-18.0) and longitudes (82.0 - 84.0). These are then put into a list of dictionaries for each meteorite, along with a index number and a randomly generated composition. The list is then entered into a JSON file (meteorites.json), with the single key for the list designated as "sites".

calculate_trips.py is second. It reads in meteorites.json and loops through the sites list, finding the travel time needed for the robot to get to the current meteorite and the time needed to take a sample. It prints this out, and at the end, prints the total number of meteorites sampled (as legs of the trip) and the total time elapsed.

## Instructions

to run the scripts, first clone the repo and make sure you are in this homework2 folder. on the command line, run "python3 generate_sites.py" first to create a new set of meteorites. They are present in the meteorites.JSON file if you want to look at them with cat command. After this, run "python3 calculate_trips.py" to run the robot simulation, which should then print out the trip information. Each leg is printed first with the time needed to get to the meteorite from the robot's last position and the time needed to take a sample, which is different depending on the meteorites composition. The last line shows the total legs of the trip and the total time elapsed to travel and take samples.

