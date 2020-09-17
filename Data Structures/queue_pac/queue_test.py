import queue_pac.queue as queue

my_queue = queue.queue_of(1, 2, 3, 4, 5, 6)

print(my_queue.to_string())

print(my_queue.dequeue())

print(my_queue.to_string())
