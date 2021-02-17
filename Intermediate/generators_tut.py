import sys

# def my_generator():
#     yield 2
#     yield 5
#     yield 12
#     yield 6

# for i in my_generator():
#     print(i)

# def fibonacci(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a+b

# for i in fibonacci(20):
#     print(i)

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

print(sys.getsizeof(first_tn(100000)),'List')
print(sys.getsizeof(firsttn_generator(100000)),'Generator')