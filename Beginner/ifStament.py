is_male = True
is_tall = True

if is_male and not is_tall:
    print("You are male or tall or both")
else:
    print("You are neither male or tall")

''' 
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

 '''
# print(max_num(300, 40, 5))
''' num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == '+':
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '/':
    print(num1/num2)
elif op == '*':
    print(num1*num2)
else:
    print("Invalid operator") '''


monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar":"March",
    "Apr": "April",
    1: "Hello"
}

print(monthConversions.get("Mar","Invalid"))
