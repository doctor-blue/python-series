""" myset = set()

myset.add(1)
myset.add(2)
myset.add(2)
myset.add(3)

myset.remove(3)
myset.discard(5)


## print(myset.pop())

for i in myset:
    print(i)

if 1 in myset:
    print("True")



print(myset)
 """

oods = {1, 3, 5, 7, 9}

evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = oods.union(evens)

print(u)

# lay ra phan tu giong nhau
i = oods.intersection(primes)

print(i)

# diff=evens.difference(primes) - lay ra ptu khac nhau trong evens so voi primes

# lay ra ptu khac nhau giua ca hai sets
diff = evens.symmetric_difference(primes)

print(diff)

""" 
evens.update(primes)

print("Updated = ", evens) """


""" 
Xoa di ptu khac nhau giua evens va primes va update cho evens
evens.intersection_update(primes)

print("Updated = ", evens) """

""" Xoa di ptu giong nhau giua evens va update cho evens
evens.difference_update(primes)

print("Updated = ", evens) """



""" 
Xoa di ptu giong nhau giua evens va update tat ca phan tu khac nhau giua 2 set cho evens
evens.symmetric_difference_update(primes)

print("Updated = ", evens) """

setA={2,4,6}
## xem setA co phai sub set cua evens hay k
## print(setA.issubset(evens))

## Xem  evens co phai set cha cua setA hay k
print(evens.issuperset(setA))

a= frozenset("HAHAHA")

print(a)







