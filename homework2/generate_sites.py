import json
import random

data = {}
sites = []

for i in range(5):

    current = {}
    current["site_id"] = i + 1

    lat = random.uniform(16.0, 18.0)

    current["latitude"] = lat

    long = random.uniform(82.0, 84.0)


    current["longitude"] = long

    comp = random.uniform(0,3)

    current["composition"] = "stony" if comp < 1 else "stony-iron" if comp < 2 else "iron"

    sites.append(current)

data["sites"] = sites

with open('meteorites.json', 'w') as out:
    json.dump(data, out, indent = 1)

