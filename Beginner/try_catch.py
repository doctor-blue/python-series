# try:
#     value = 10/0
#     num = int(input("Enter a number: "))
#     print(num)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("Invalid input ")

try:
    #value = 10/0
    num = int(input("Enter a number: "))
    print(num)
except Exception as err:
    print(err)
except ValueError:
    print("Invalid input ")
else:
    print("Every thing is fine")
finally:
    print("Finally run")