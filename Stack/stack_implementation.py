class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        if element not in self.stack:
            self.stack.append(element)
            return True
        else:
            print('Element found in stack already')
            return False

    def peek(self):
        if (len(self.stack)):
            print(self.stack[-1])
            return True
        else:
            print('Stack is empty.')
            return False

    def pop(self):
        if len(self.stack):
            self.stack.remove(self.stack[-1])
            return True
        else:
            print('Stack is empty.')
            return False


stack = Stack()
stack.push(5)
stack.peek()
stack.push(7)
stack.peek()
stack.push(3)
stack.peek()
stack.pop()
stack.peek()
stack.pop()
stack.peek()
stack.pop()
stack.peek()