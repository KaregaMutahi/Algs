class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items ==[]
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items)-1]

s = Stack()
s.push('hello')
s.push('True')
s.push ('World')
print (s.peek())

