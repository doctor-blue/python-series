import sys
import timeit

myTuples = ("Max", 20, "New york")

myList = ["Max", 20, "New york"]

""" print(myTuples)

## item=[x+x for x in myTuples]
items = list(myTuples)

print(type(items))

print(myTuples.count("Maxx"))

name, age, address = myTuples

print(name)
print(age)
print(address)

i,*i1=myTuples

print(i)
print(i1) """

print(sys.getsizeof(myTuples), "bytes")
print(sys.getsizeof(myList), "bytes")

# print(timeit.timeit(stmt="(15, 20, 1)", number=1000000))
# print(timeit.timeit(stmt="[15, 20, 1]",number= 1000000))
