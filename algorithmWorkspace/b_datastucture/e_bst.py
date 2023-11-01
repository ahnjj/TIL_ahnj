from c_stack import Stack
from d_queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return self.data
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.length = 0

    def __len__(self):
        return self.length

    def insert(self, data):
        node = Node(data)
        
        if self.root is None:
            self.root = node
            self.length += 1
            return

        link = self.root

        while True:
            if data <= link.data:
                if link.left_child is None:  # left가 비어있으면 거기에 넣기
                    link.left_child = node
                    break

                link = link.left_child
            else:
                if link.right_child is None:
                    link.right_child = node
                    break
                link = link.right_child
        self.length += 1

    def find(self, data):
        link = self.root
        while True:
            if link is None: return False
            if data == link.data : return 
            
            if data < link.data:
                link = link.left_child
            else:
                link = link.right_child

    # preorder traversal
    def pre_order(self, link):
        res = []
        if link is not None:
            res += [link.data] # root 넣어주기

        if link.left_child is not None: # 왼쪽 노드가 있을 경우
            res += self.pre_order(link.left_child)  # left recursion

        if link.right_child is not None:
            res += self.pre_order(link.right_child) # right recursion

        return res
    
        
    # recursion없이 stack으로 pre-order순회 구현
    def pre_order2(self, root):
        s1 = Stack()
        s2 = []

        # root 넣기
        if root is not None:
            s1.push(root)
        else:
            return s2
        
        while not(s1.is_empty()):
            root = s1.pop()
            s2.append(root.data)

            if root.left_child is not None:
                s1.push(root.left_child)
            # left 없다
            elif root.right_child:
                s1.push(root.right_child)

        return s2

            


                

            
        







