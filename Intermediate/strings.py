my_string = "I'm the doctor"

my_string1 = """\
Hello 
World\
"""


subString = my_string[:5]
# Dao ngc chuoi
## subString= my_string[::-1]

print(subString)

if 'e' in my_string:
    print("Yes")
else:
    print('No')

my_string = '   Hello world   '
my_string = my_string.strip()
print(my_string)

print(my_string.upper())

print(my_string.startswith('Hello'))

print(my_string.find('lo'))

print(my_string.replace("world", "New Universe"))

val = 3.1223

my_string = "The variable is %f" % val

my_string = "The variable is {:.2f}".format(val)

my_string = f"The variable is {val}"

print(my_string)
