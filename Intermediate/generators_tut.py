import sys


def my_generator():
    yield 1
    yield 2
    yield 3

# g= my_generator()


""" for i in g:
    print(i) """

""" value = next(g)

print(value) """

# rint(sum(g))

# print(sorted(g))


def count_down(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1


""" cd = count_down(5)

value = next(cd)

print(value)
print(next(cd)) """


def first_tn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def firsttn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


""" print(sys.getsizeof(first_tn(100000)))
print(sys.getsizeof(firsttn_generator(100000))) """


def fibonacci(limit):
    # do some thing
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b


""" fib=fibonacci(20)

for i in fib:
    print(i)
 """

my_generator1 = (i for i in range(10) if i % 2 == 0)
print(list(my_generator1))

my_list=[i for i in range(10) if i % 2 == 0]
print(my_list)
""" for i in my_generator1:
    print(i)
 """

 # my_generator1 < my_list