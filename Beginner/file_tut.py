employees_file = open('employees.txt', 'r')

# print(employees_file.readline())
# print(employees_file.readlines())

for i in employees_file.readlines():
    print(i)

employees_file.close()

# employees_file = open('employees.txt', 'w')

employees_file = open('employees.txt', 'a')
employees_file.write("\nWelcom to my channel")
employees_file.close()