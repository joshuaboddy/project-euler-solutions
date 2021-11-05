import math

grid = 123
str_grid = str(grid)
biggest_prod = 0
s = 0
while s <= len(str_grid) - 4:
    to_prod = str_grid[s:s+4]
    prod = math.prod([int(x) for x in to_prod])
    if prod > biggest_prod:
        biggest_prod = prod
    s = s+4
    