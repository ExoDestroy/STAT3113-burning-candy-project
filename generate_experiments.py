import csv
from random import shuffle

TRIALS = 45
REPLICATES = 5
BRANDS = ["Jujyfruits", "Mike and Ike", "Dots"]
FLAVORS = ["Lime", "Orange", "Lemon"]

data = []

# Replicates each of the 9 treatments 5 times.
for b in BRANDS:
    for f in FLAVORS:
        for i in range(REPLICATES):
            data.append([b, f, '-'])

# Randomizes experiment order (except first line for the column names).
shuffle(data)
data.insert(0, ["Brand", "Flavor", "Time (s)"])

# Creates a csv file
with open("burning_candy.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

