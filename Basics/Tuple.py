# Tuples are immutable means once you create it you can't change it.
coordinates = (4, 5)
coordinates_in = [(4, 5), (3, 5)] # Tuples inside list and they can be changed.
print(coordinates)

# Learn more
tup = (1, 2, 3, 'a', "string")
print(tup)

# accessing element
print(tup[0])
# tup[0] = 100 # this is not valid

# Tuple unpacking
x, y, z, a, b = tup
print(x) # means tuple right up there x = 1, y = 2, z = 3

# Tuple concatenation
tup1 = (1, 2, 30)
tup2 = ('a', 'b')
print(tup1 + tup2)
print(len(tup))
