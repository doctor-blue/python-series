import sys

my_tuple = ("Max",20,"New York")
my_list = ["Max",20,"New York"]

# print(my_tuple)
# for i in my_tuple:
#     print(i)
# items = list(my_tuple)
# print(type(items))

# print(my_tuple.count("Max"))

name,age, address = my_tuple

print(name,age,address)
i, *i1 = my_tuple

print(i)
print(type(i1))

print(sys.getsizeof(my_tuple),"bytes")
print(sys.getsizeof(my_list),"bytes")