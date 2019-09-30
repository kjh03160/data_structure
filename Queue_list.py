class Queue:
    def __init__(self):
        self.item = []
        self.size = 0
        self.front_index = 0

    def enqueue(self, value):
        self.item.append(value)
        self.size += 1

    def dequeue(self):
        if self.size != 0:
            return_val = self.item[self.front_index]
            self.front_index += 1
            self.size -= 1
            return return_val
        else:
            print("Queue is Empty")

    def print_queue(self):
        print("front",'-> ', end="")
        for i in self.item:
            print(i ,'->', end=" ")
        print('end')

q = Queue()
q.enqueue(1)
q.print_queue()