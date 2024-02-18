import random
from queue import Queue


class ServiceCenter:
    def __init__(self):
        self.queue = Queue()

    def generate_request(self):
        new_request = "".join(random.choices("abcdefg", k=5))
        self.queue.put(new_request)
        print(f"New request: {new_request}")

    def process_request(self):
        if self.queue.empty():
            print("Queue is empty!")
            return
        current_request = self.queue.get()
        print(f"Request {current_request} is being processed")
        print(f"Request {current_request} has been processed")


if __name__ == "__main__":
    sc = ServiceCenter()
    while True:
        sc.generate_request()
        sc.process_request()
