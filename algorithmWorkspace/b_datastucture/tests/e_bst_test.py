import unittest
import sys
from e_bst import *
sys.path.append(r'/Users/jeong_ahn/TIL/algorithmWorkspace/b_datastructure/tests')


class BSTQTest(unittest.TestCase):
    def test_pre_order(self):
        bst = BinarySearchTree()
        for i in [8,3,10,1,6,14,4,7,13]:
            bst.insert(i)

        print('preorder:', bst.pre_order(bst.root))
        
    def test_pre_order2(self):
        bst = BinarySearchTree()
        for i in [8,3,10,1,6,14,4,7,13]:
            bst.insert(i)

        print('preorder2:', bst.pre_order2(bst.root))


if __name__ == '__main__':
    unittest.main()
