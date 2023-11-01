import unittest
import sys
sys.path.append(r'/Users/jeong_ahn/TIL/algorithmWorkspace/b_datastructure/tests/a_list_q_test.py')
from a_list_q import *

class ListQTest(unittest.TestCase):
    def test_str(self):
        texts = ['tomato', '토마토', '기러기' ,'Wild goose', '역삼역', 'Yeoksam station']
        for text in texts:
            if(check_palindrome(text)):
                print(text + ' 는 회문입니다.')

if __name__ == '__main__':
    unittest.main()
