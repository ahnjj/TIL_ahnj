import unittest
import sys
from b_hashtable_q import *
sys.path.append(r'/Users/jeong_ahn/TIL/algorithmWorkspace/b_datastructure')

class HashTableQTest(unittest.TestCase):
    def test_q1(self):        
        texts = ['hashtable', 'samsung', 'aabb']
        for text in texts:
            print(q1(text))

if __name__ =="__main__":
    unittest.main()
