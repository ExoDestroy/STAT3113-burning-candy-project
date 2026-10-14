import csv
from random import choice as rv

CANDY_BRAND = ["Jujyfruits", "Mike and Ike", "Dots"]

CANDY_FLAVOR = ["Lime", "Orange", "Lemon"]

TRIALS = 45

data = [ ["Brand", "Flavor"] ]

for i in range(TRIALS):
    data.append([rv(CANDY_BRAND), rv(CANDY_FLAVOR)])

# Creates a readable txt file
with open("experiment_list.txt", "w") as file:
    for i in range(TRIALS):
        # Formats numbered trials so each one has same indentation
        file.write(f"{(i+1)})" + " " * (5 - (i > 8)))
        # The function rv chooses random value from brand/flavor list
        file.write(f"Brand: {data[i+1][0]}")
        # Ensures similar spacing regardless of the length of candy brand name
        file.write(" " * ((len(max(CANDY_BRAND, key=len)) - len(data[i+1][0])) + 10))
        file.write(f"Flavor: {data[i+1][1]}\n" + "-" * 70 + "\n")

# Creates a csv file
with open("burning_candy.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)