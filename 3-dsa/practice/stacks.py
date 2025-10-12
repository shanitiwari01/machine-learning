class Stacks:
    def __init__(self):
        self.items = []

    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    
    def add(self, item):
        return self.items.append(item)
    
    def remove(self):
        return self.items.pop()
    
    def get(self):
        return self.items
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0

stack = Stacks();

stack.add(1)
stack.add(2)
stack.add(3)

print(stack.get())

stack.remove()

print(stack.get())

print(stack.size())

print(stack.peek())

stack.remove()

print(stack.peek())

stack.remove()

print(stack.peek())