class Stack:
    def __init__(self):
        self.storage = []

    def size(self):
        return len(self.storage)

    def is_empty(self):
        return self.size() == 0

    def push(self, value):
        self.storage.insert(0, value)
        return self

    def pop(self):
        return self.storage.pop(0)

    def peek(self):
        return self.storage[0]

    def to_string(self):
        print('=====top=====')
        for i in self.storage:
            print(f'     {i}')
        print('======bottom====')


def create(values):
    if isinstance(values, list):
        stack = Stack()
        for i in values:
            stack.push(i)
        return stack
    return None


def stack_of(*args):
    stack = Stack()
    for i in args:
        stack.push(i)
    return stack
