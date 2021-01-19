friends = ["Sam", "John", "Anna", "Tan"]
print(friends)
# friends.pop(1)
# del friends[2]
# friends.clear()

# for i in range(len(friends)):
#     print(friends[i])

# [print(x) for x in friends]
# friends.sort()
# print(friends)
# numbers = [50, 9, 0, 15, 80]
# numbers.sort(reverse = True)
# print(numbers)

# friends.reverse()
# print(friends)

# friends2 = friends.copy()
# friends2 = list(friends)

# friends2.append(25)
# print('friends2', friends2)
# print('friends1', friends)

numbers = list((1, 5, 9, -2))
print(numbers)

# list3 = friends+numbers
# print("List 3 = ", list3)

friends.extend(numbers)
print('friends = ',friends)
