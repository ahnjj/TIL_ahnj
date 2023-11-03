import random
import unittest
import sys
from b_selection_sort import *
sys.path.append(r'/Users/jeong_ahn/TIL/algorithmWorkspace/d_bruteforce')

class SelectionSortTest(unittest.TestCase):
    def test_selection_sort(self):
        arr = [round(random.randrange(1,1000)) for _ in range(1000)]
        print(selection_sort(arr))


if __name__ == '__main__':
    unittest.main()
