import argparse
import csv
from random import shuffle

# Utilized argparse in case we decide to change the trials or factors later.
parser = argparse.ArgumentParser()
parser.add_argument("--trials", type=int)
parser.add_argument("--brand", nargs='+', type=str, help='A list of candy brand names')
parser.add_argument("--flavor", nargs='+', type=str, help='A list of candy flavors')
# Currently decided trial count and factors.
parser.set_defaults(trials=45, brand=["Jujyfruits", "Mike and Ike", "Dots"], flavor=["Lime", "Orange", "Lemon"])
args = parser.parse_args()

if args.trials < 0:
    parser.error("--trials must be positive")

if args.brand is None or args.flavor is None:
    parser.error("--brand/--flavor must have input")

treatments = len(args.brand) * len(args.flavor)

if args.trials % (len(args.brand) * len(args.flavor)):
    parser.error(f"""Ensure trials / treatments divides evenly for equal number of each replicate.
                    {args.trials} % {treatments} != 0                    
                 """)

data = []
replicate_count = args.trials // treatments

# Replicates each treatment (trials / treatment) times.
for b in args.brand:
    for f in args.flavor:
        for i in range(replicate_count):
            data.append([b, f, 0])

# Randomizes experiment order (except first line for the column names).
shuffle(data)
data.insert(0, ["Brand", "Flavor", "Time (s)"])

# Creates a csv file
with open("burning_candy.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Only write to brand & flavor columns
    writer.writerows(data)

