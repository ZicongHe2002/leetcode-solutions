from collections import deque
from threading import Lock, Semaphore


class BoundedBlockingQueue:
    def __init__(self, capacity):
        self.queue = deque()
        self.lock = Lock()
        self.slots = Semaphore(capacity)
        self.items = Semaphore(0)

    def enqueue(self, element):
        self.slots.acquire()
        with self.lock:
            self.queue.append(element)
        self.items.release()

    def dequeue(self):
        self.items.acquire()
        with self.lock:
            element = self.queue.popleft()
        self.slots.release()
        return element

    def size(self):
        with self.lock:
            return len(self.queue)
