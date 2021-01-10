# is_male = False

# if is_male :
#     print("Is male")
# else:
#     print("Is female")

# num_1 = 25
# num_2 = 60
# num_3 = 30

# if num_1 >= num_2 and num_1 >= num_3:
#     print("Max = ", num_1)
# elif num_2 >= num_1 and num_2 >= num_3:
#     print("Max = ", num_2)
# else:
#     print("Max = " ,num_3)

# if num_1 >= num_2 or num_1 >= num_3:
#     print(num_1)

num_1 = float(input("Enter first number  =  "))
num_2 = float(input("Enter second number  =  "))
op = input("Enter operator ")

if op == '+':
    print(num_1, op, num_2, ' = ', num_1+num_2)
elif op == '-':
    print(num_1, op, num_2, ' = ', num_1-num_2)
elif op == '-':
    print(num_1, op, num_2, ' = ', num_1*num_2)
elif op == '-':
    print(num_1, op, num_2, ' = ', num_1/num_2)
else:
    print("Invalid Operator ")


