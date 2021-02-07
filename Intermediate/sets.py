# my_set1 = set()
# my_set1.add(1)
# my_set1.add(6)

# my_set1.add(8)
# my_set1.add(9)

# my_set1.remove(8)


# if 1 in my_set1:
#     print("True")

oods = {1,3,5,7,9}
evens = {2,4,6,8}
primes = {2,3,5,7}

# u = oods.union(evens)

# print(u)

# i = oods.intersection(primes)
# print(i)

diff = evens.symmetric_difference(primes)

print(diff)