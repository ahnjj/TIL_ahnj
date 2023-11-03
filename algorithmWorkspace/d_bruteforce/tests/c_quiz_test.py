import unittest
import sys
from c_quiz import *
import random
sys.path.append(r'/Users/jeong_ahn/TIL/algorithmWorkspace/d_bruteforce')

class QuizTest(unittest.TestCase):
    def test_q1(self):
        arr = [1666, 3636, 5555, 6666, 3666, 79999, 60666]
        print(doom_day(arr, 4))

    def test_q2(self):
        arr = [round(random.randrange(10,15)) for _ in range(7)]
        t = 100 - sum(arr)
        arr[6] = arr[6] + t
        
        arr.append(round(random.randrange(1,20)))
        arr.append(round(random.randrange(1,20)))
        self.assertEqual(sum(q2(arr)), 100)


if __name__ == '__main__':
    unittest.main()