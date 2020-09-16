import random
import secrets

# a = random.random()
# a =random.uniform(1,10)
# a =random.randint(1,10)
# a =random.normalvariate(1,10)

myList = list("ABCDEFGHKLMN")
# a = random.choice(myList)
# a=random.sample(myList,3)
# a=random.choices(myList,k=3)

''' random.shuffle(myList)
print(myList) '''

''' random.seed(100,2)
print(random.random())
print(random.randint(1,10)) '''

#a= secrets.randbits(4)
a=secrets.choice(myList)
print(a)