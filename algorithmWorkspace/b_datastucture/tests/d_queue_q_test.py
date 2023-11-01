import unittest
import sys
from d_queue_q import *
sys.path.append(r'/Users/jeong_ahn/TIL/algorithmWorkspace/b_datastructure/tests')


class QueueQTest(unittest.TestCase):
    def test_q1(self):
        print(q1(7))
    def test_q2(self):
        print(q2(7, 3))


if __name__ == '__main__':
    unittest.main()