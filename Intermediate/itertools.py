from itertools import product
from itertools import permutations
from itertools import combinations


a = [1, 2,3]
b = [3, 4]
prod = product(a, b, repeat=2)
print(list(prod))

perm = permutations(a,2)
print(list(perm))

comb=combinations()
