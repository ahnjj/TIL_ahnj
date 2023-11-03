import random
import unittest
import sys
from a_bubble_sort import *
sys.path.append(r'/Users/jeong_ahn/TIL/algorithmWorkspace/d_bruteforce')

class SortTest(unittest.TestCase):
    def test_bubble_sort(self):
        arr = [round(random.randrange(1,1000)) for _ in range(1000)]
        # print(bubble_sort(arr))
        print(bubble_sort2(arr))

if __name__ == '__main__':
    unittest.main()