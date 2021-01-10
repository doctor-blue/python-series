import random
import secrets

# a = random.random() #0 -> 1
# print(a)

# print(random.uniform(1, 10))
# print(random.randint(5, 100))
myList1 = [5, 4, 9, 2, 55, "Hi", True]

myList ="QWERTYUIOP" #"JOHNSMITHFROMVIETNAM"
# print(random.choice(myList1))
print(random.sample(myList, 5))
print(random.choices(myList, k=5))
# random.shuffle(myList1)
# print(myList1)

# random.seed(2)
# print(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))

# random.seed(2)
# print(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
