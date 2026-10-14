from random import choice as rv

CANDY_BRAND = ["Jujyfruits", "Mike and Ike", "Dots"]

CANDY_FLAVOR = ["Lime", "Orange", "Lemon"]

TRIALS = 45

with open("experiment_list.txt", "w") as file:
    for i in range(TRIALS):
        brand = rv(CANDY_BRAND)
        # Formats numbered trials so each one has same indentation
        file.write(f"{(i+1)})" + " " * (5 - (i > 8)))
        # The function rv chooses random value from brand/flavor list
        file.write(f"Brand: {brand}")
        # Ensures similar spacing regardless of the length of candy brand name
        file.write(" " * ((len(max(CANDY_BRAND, key=len)) - len(brand)) + 10))
        file.write(f"Flavor: {rv(CANDY_FLAVOR)}\n" + "-" * 70 + "\n")