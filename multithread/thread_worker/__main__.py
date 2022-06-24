from multiprocessing import Process, Queue, Event
import time
from .worker import dispatcher


def main():
    """
    :return:
    """
    exit_event = Event()
    task_q = Queue(20)
    worker_proc = Process(target=dispatcher, args=(task_q, exit_event))
    worker_proc.start()

    for i in range(100):
        time.sleep(1)

        print(f'sending {i}')
        task_q.put(i)

    exit_event.set()
    worker_proc.join()


if __name__ == "__main__":
    main()
