class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        // Add your solution here!

    def pop(self):
        // Add your solution here!

    def peek(self):
        // Add your solution here!

    def is_empty(self):
        // Add your solution here!

if __name__ == '__main__':
    stack = Stack()
    stack.push(5)
    stack.push(10)
    stack.push(15)
    print(stack.pop())  # Expected: 15
    print(stack.peek())  # Expected: 10
    print(stack.is_empty())  # Expected: False
