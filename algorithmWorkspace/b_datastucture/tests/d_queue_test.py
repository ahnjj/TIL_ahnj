import unittest
import sys
from b_datastucture.d_queue import *
sys.path.append(r'/Users/jeong_ahn/TIL/algorithmWorkspace/b_datastructure/tests')


class QueueTest(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        for i in range(10):
            queue.enqueue(i)

        print(queue)

    def test_dequeue(self):
        queue = Queue()
        for i in range(10):
            queue.enqueue(i)

        for i in range(10):
            print(queue.dequeue(), end='')

        print(queue)

if __name__ == '__main__':
    unittest.main()