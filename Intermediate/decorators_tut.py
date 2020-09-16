import functools


def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper


@start_end_decorator
def print_name():
    print('Alex')


@start_end_decorator
def add5(x):
    return x+5


# print_name= start_end_decorator(print_name)
""" 
print_name()
result = add5(15)
print(result) """
""" 
print(help(add5))
print(add5.__name__) """

""" @mydecorator
def do_some_thing():
    pass """
"""  def wrapper(*args, **kwargs):
               for _ in range(times):
                   result = func(*args, **kwargs)+_
               return result
           return wrapper """


def repeat(times):

    def decorator_func(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_func


""" @repeat(2)
@start_end_decorator
@repeat(3)
def greet(name):
    print(f"Hello {name}")
    return 2 """


# greet("a")
""" kq = greet('John')
print(type(kq))
print(kq) """


class CountCalls:
    def __init__(self, func):
        super().__init__()
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        print('Hi there')
        self.num_calls += 1
        print(f'This executed {self.num_calls} times')
        return self.func(*args, **kwargs)


""" cc = CountCalls(None)
cc() """


@repeat(3)
@CountCalls
def say_hello():
    print('Hello')


say_hello()
