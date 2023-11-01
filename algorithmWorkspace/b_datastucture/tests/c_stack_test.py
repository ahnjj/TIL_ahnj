import unittest
import sys
from c_stack import *
sys.path.append(r'/Users/jeong_ahn/TIL/algorithmWorkspace/b_datastructure/tests/c_stack_test.py')

class StackTest(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        print(stack)


    def test_pop(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        for i in range(10):
            print(stack.pop(), end=' ')
        print(stack)

    def test_peek(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        for i in range(10):
            print(stack.peek(), end=' ')
        print(stack)


if __name__ == '__main__':
    unittest.main()
