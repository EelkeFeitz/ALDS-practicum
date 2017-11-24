class mystack:

    def __init__(self):
        self.stack = []

    def push(self, a):
        self.stack.append(a)

    def pop(self):
        self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def isEmpty(self):
        return not bool(len(self.stack))

thing = mystack()
thing.push(5)
thing.push(6)
print('Huidige stack:      ', thing.stack)
print('Laaste van de stack:', thing.peek())
print('Is de stack leeg?:  ', thing.isEmpty())
print('Pop van de stack:   ', thing.stack.pop())
print('Huidige stack:      ', thing.stack)
print('Laaste van de stack:', thing.peek())
print('Pop van de stack:   ', thing.stack.pop())
print('Huidige stack:      ', thing.stack)
print('Is de stack leeg?:  ', thing.isEmpty())