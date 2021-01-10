# def print_user_name(first_name, last_name):
#     print('First name = ', first_name, ' Last name = ', last_name)


# print_user_name('john')
# print_user_name('sam')
# print_user_name('tan')
# print_user_name('nguyen')

# def pow(x, y):
#     return x**y


# num = pow(y=2, x=3)
# print('Num = ', num)


# def my_function(*args):
#     for arg in args:
#         print(arg)
# def my_function(*args):
#     print('args[0]',args[4])

# my_function("John",18,"Smith",30)
# print('========================')
# my_function('Apple')
# my_function()

# def my_function(**kid):
#     print('First name = ', kid['first_name'])


# my_function(first_name2="John")

def pow(x, y=2):
    return x**y


num = pow(3, 3)
print('Num = ', num)
