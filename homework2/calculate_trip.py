import json
import math
mars_radius = 3389.5

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )


with open('meteorites.json', 'r') as f:
    ml_data = json.load(f)

robopos = [16.0, 82.0]
totaltime = 0
for i in range(len(ml_data["sites"])):
    
    leg = i + 1

    current = ml_data["sites"][i]

    nextDist = calc_gcd(robopos[0], robopos[1], current["latitude"], current["longitude"])

    traveltime = round(nextDist/10, 2)

    sampletime = 1 if current["composition"] == "stony" else 2 if current["composition"] == "iron" else 3

    print("leg", leg, ": travel time =", traveltime, "hr, sample time =", sampletime, "hr")

    totaltime += traveltime + sampletime

    robopos[0] = current["latitude"]
    robopos[1] = current["longitude"]

print ("=====================================")

print (5, "total legs: total time elapsed = ", totaltime, " hr")



