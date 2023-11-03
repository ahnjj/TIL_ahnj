import unittest
import sys
from e_bst import *
sys.path.append(r'/Users/jeong_ahn/TIL/algorithmWorkspace/b_datastructure/tests')


class BSTQTest(unittest.TestCase):
    def test_dfs(self):
        bst = BinarySearchTree()
        for i in [8,3,10,1,6,14,4,7,13]:
            bst.insert(i)

        # print('preorder:', bst.pre_order(bst.root))
        # print('preorder:', bst.pre_order_stack())
        # print('inorder:', bst.in_order(bst.root))
        # print('inorder stack:', bst.in_order_stack())
        print('inorder stack2:', bst.in_order_stack2())
        # print('postorder:', bst.post_order(bst.root))
        # print('postorder stack:', bst.post_order_stack())

    def test_bfs(self):
        bst = BinarySearchTree()
        for i in [8,3,10,1,6,14,4,7,13]:
            bst.insert(i)
        print('bfs: ', bst.bfs())
        


if __name__ == '__main__':
    unittest.main()
