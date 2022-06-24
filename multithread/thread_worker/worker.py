from multiprocessing import Process, Queue, Event
from threading import Thread

import time


def task_handler(q):
    """
    :return:
    """
    print('worked tread started')
    while True:
        task = q.get()
        print(f'received {task}')


N_Threads = 5
def dispatcher(q: Queue, exit_event: Event):
    """
    :return:
    """
    for _ in range(N_Threads):
        worker = Thread(target=task_handler, args=(q,))
        # daemon thread means a thread that will end when the main thread ends
        worker.daemon = True
        worker.start()

    while not exit_event.is_set():
        time.sleep(1)
        print('.')
