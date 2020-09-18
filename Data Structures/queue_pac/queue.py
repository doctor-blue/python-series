class Queue:
    def __init__(self):
        self.storage = []

    def count(self):
        return len(self.storage)

    @property
    def is_empty(self):
        return self.count() == 0

    def enqueue(self, element):
        self.storage.insert(self.count(), element)

    def dequeue(self):
        if self.is_empty:
            return None
        else:
            return self.storage.pop()

    def to_string(self):
        strings = ""
        for i in self.storage:
            strings += f'| {i}'
        return f'- font - {strings}  - back -'


def create(values):
    if isinstance(values, list):
        queue = Queue()
        for i in values:
            queue.enqueue(i)
        return queue
    return None


def queue_of(*args):
    queue = Queue()
    for i in args:
        queue.enqueue(i)
    return queue
