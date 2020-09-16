import multiprocessing
import threading
import os
import time


def run():
    def square_numbers():
        for i in range(100):
            i*i
            time.sleep(0.2)

    threads = []
    num_threads = 10

    for i in range(num_threads):
        p = threading.Thread(target=square_numbers)
        threads.append(p)

    for p in threads:
        p.start()

    for p in threads:
        p.join()

    print("End main")


if __name__ == '__main__':
    run()


def calc_square(numbers, q):
    for n in numbers:
        q.put(n*n)
        time.sleep(0.2)

    q.put(-1)
    print('Exiting function')


if __name__ == '__main__':
    print('Now in the main code. Process name is:', __name__)
    numbers = [2, 3, 4, 5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(numbers, q))
    p.start()

    while True:
        nq = q.get()
        print('Message is:', nq)
        if nq == -1:
            break

    print('Done')
    print(os.cpu_count())
    p.join()
