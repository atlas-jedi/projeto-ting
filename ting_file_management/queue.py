from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data = []
        self.__length = 0

    def __len__(self):
        return self.__length

    def __str__(self):
        return self.data

    def enqueue(self, value):
        self.data.append(value)
        self.__length += 1

    def dequeue(self):
        item_removed = self.data[0]
        self.data.pop(0)
        self.__length -= 1
        return item_removed

    def search(self, index):
        if not isinstance(index, int) or (self.__length <= index) or index < 0:
            raise IndexError("Índice Inválido ou Inexistente")
        return self.data[index]
