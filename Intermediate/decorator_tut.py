import functools
# def say_hi():
#     def say_hi_again():
#         print('Hello')
#     return say_hi_again


# greet = say_hi()

# greet()


# def greet(name):
#     return 'Hello ' + name


# def call_func(greet):
#     other_name = 'John'
#     return greet(other_name)

# print(call_func(greet))

# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print("Start")
#         result = func(*args,**kwargs)
#         print('End')
#         return result
#     return wrapper

# @start_end_decorator
# def print_name():
#     print("Alex")


# print_name()

def repeat(times):
    def decorator_func(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(times):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decorator_func

@repeat(5)
def print_name():
    print('John')


print_name()