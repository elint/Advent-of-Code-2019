import math

# module fuel value is floor(moduleMass/3)-2
def calcFuel(mass):
    fuel = math.floor(int(mass) /3) - 2
    if fuel > 0:
        return fuel + calcFuel(fuel)
    else:
        return 0 

# sum all fuel values
totalFuel = 0

with open('input') as fp:
    line = fp.readline()
    while line:
        totalFuel += calcFuel(int(line))
        line = fp.readline()
print(totalFuel)
fp.close