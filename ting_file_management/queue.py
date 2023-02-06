from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if len(self.data) == 0:
            return None

        return self.data.pop(0)

    def search(self, index):
        size = len(self.data)

        if not index >= 0 and index <= size:
            raise IndexError

        return self.data[index]
