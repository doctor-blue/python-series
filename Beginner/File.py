
employee_file = open("employees.txt","r")

print(employee_file.readline())
print(employee_file.readlines()[0])

for i in employee_file.readlines():
    print(i)


employee_file.close()

employee_file=open("hahaha.html","a")
employee_file.write("<p>Hello World - Coder</p>")
employee_file.close()
