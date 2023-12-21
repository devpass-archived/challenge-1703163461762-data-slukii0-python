import unittest
from main import Stack

class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(5)
        self.assertEqual(stack.stack, [5])
        stack.push(10)
        self.assertEqual(stack.stack, [5, 10])

    def test_pop(self):
        stack = Stack()
        stack.push(5)
        stack.push(10)
        stack.push(15)
        self.assertEqual(stack.pop(), 15)
        self.assertEqual(stack.stack, [5, 10])

    def test_peek(self):
        stack = Stack()
        stack.push(5)
        stack.push(10)
        stack.push(15)
        self.assertEqual(stack.peek(), 15)
        self.assertEqual(stack.stack, [5, 10, 15])

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(5)
        self.assertFalse(stack.is_empty())

if __name__ == '__main__':
    unittest.main()
