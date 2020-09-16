from math import *
from main2 import *

character_name = "John Smith"
print("Hello world, My name is ", character_name)
character_age = -35
is_my_time = True
print(character_name.isupper())
print(len(character_name))
print(character_name[0])
print(character_name.index("n"))
print(character_name.replace("John", "Data"))
print(str(character_age))
print(abs(character_age))
print(pow(character_age, 2))
print(max(2, 5, 6))
print(round(3.5926488))
print(floor(3.6894154))
# print(sqrt(36))
"""
user_name = input("What your name? ")
age = input("How old are you ?")
print("Hello ", user_name, " You are ", age)
"""
"""
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + int(num2)
print(result)
"""
friends = ["John", "Jim", "2.6", "Toby"]
age_of_my_friends = [20, 60, 50, 8, 7]
# friends.append("hello")
# friends.insert(1, 5)
# friends.remove("Toby")
# friends.pop()
print(friends)
print(friends.index("Toby"))
print(friends.count("John"))
friends.sort()
print(friends)
age_of_my_friends.reverse()
print(age_of_my_friends)
say_hi("haha",56)
