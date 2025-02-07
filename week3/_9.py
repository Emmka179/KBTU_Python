def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    return chickens, rabbits
numheads, numlegs = 35, 94
print(solve(numheads, numlegs))