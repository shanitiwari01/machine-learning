class Queues:
    def __init__(self):
        self.queues = []

    def enqueue(self, element):
        return self.queues.append(element)

    def isEmpty(self):
        return len(self.queues) == 0
    
    def peek(self):
        return self.queues[0]
    
    def dequeue(self):
        return self.queues.pop(0)
    
    def get(self):
        return self.queues

queues = Queues()

queues.enqueue(1)
queues.enqueue(2)
queues.enqueue(3)

print(queues.get())

print(queues.peek())

print(queues.dequeue())

print(queues.get())
