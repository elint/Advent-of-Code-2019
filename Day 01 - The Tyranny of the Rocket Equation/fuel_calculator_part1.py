import math

# sum all fuel values
totalFuel = 0

# module fuel value is floor(moduleMass/3)-2
with open('input') as fp:
    line = fp.readline()
    while line:
        totalFuel += math.floor(int(line) / 3) - 2
        line = fp.readline()
print(totalFuel)
fp.close