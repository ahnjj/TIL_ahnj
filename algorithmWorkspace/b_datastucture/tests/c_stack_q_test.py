import unittest
import sys
from c_stack_q import *
sys.path.append(r'/Users/jeong_ahn/TIL/algorithmWorkspace/b_datastructure/tests/c_stack_q_test.py')

class StackQTest(unittest.TestCase):
    def test_q1(self):
        self.assertTrue(is_pair('{}()[]'))  # True
        self.assertTrue(is_pair('{([])}'))  # True
        self.assertFalse(is_pair('{([}])}')) # False
        self.assertFalse(is_pair('{(ㄴ[}ㅎ]ㄹㄹ)}')) # False


if __name__ == '__main__':
    unittest.main()
