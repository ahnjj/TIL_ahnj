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
    # root - root의 왼쪽 - root의 오른쪽 없으면
    # root로 다시 올라가서 (stack에서 꺼내기)
    # root의 오른쪽으로 건너감
    def pre_order_stack(self):
        stack = Stack()
        res = Queue()
        link = self.root

        while True:
           
            if link is not None:
                 # root를 stack에
                stack.push(link)
                # Queue에 root넣어주기
                res.enqueue(link.data)
                # 다 탐색하면 종료
                if len(res) == self.length: break

                # 왼쪽 자식이 있을 때
                if link.left_child is not None: 
                    link = link.left_child
                    continue
      
                stack.pop()
                # 왼쪽 없고 오른쪽 있을 때
                if link.right_child is not None:
                    link = link.right_child
                    continue
                else:
                    # 오른쪽 자식이 없을 때 부모로 올라가서 (stack이용)
                    # 부모의 오른자식으로 가야한다.
                    # stack.pop() # 하나 올라가서
                    parent = stack.pop()
                    link = parent.right_child
                
            continue
        return res

    def in_order(self, link):
        res = []

        if link.left_child is not None: # 왼쪽 노드가 있을 경우
            res += self.pre_order(link.left_child)  # left recursion
        if link is not None:
            res += [link.data] # root 넣어주기

        if link.right_child is not None:
            res += self.pre_order(link.right_child) # right recursion

        return res
            
    def in_order_stack(self):
        stack = Stack()
        res = Queue()
        link=self.root

        while True:
            # 현재 노드를 stack에
            if link is not None:
                stack.push(link)

                # 1. 가장 왼쪽으로
                if link.left_child is not None:
                    link = link.left_child
                    continue
                 
                # 넣었으면 현재 노드를 스택에서 바로 뺀다
                stack.pop()
                # 왼쪽 없으면 - 현재 노드 넣고
                res.enqueue(link.data)
                # 넣었으면 길이 확인
                if len(res) == self.length: break
                

                # 오른쪽 탐색
                if link.right_child is not None:
                    link = link.right_child
                    continue
                
            # 왼쪽 오른쪽 둘다 없을때는 위로 올라가야함
            # 위 부분 중에 아직 오른쪽 탐색 안된 곳으로 이동(왼쪽 방문했는지 검토)
            parent = stack.pop()
            res.enqueue(parent.data) # 부모 노드 넣고
            if len(res) == self.length: break # 넣었으면 길이 확인
            link = parent.right_child # 부모의 오른쪽으로
                
        return res
    
    # 오류남
    def in_order_stack2(self):
        stack = Stack()
        res = Queue()
        link = self.root
        
        while True:
            if link is not None:
                stack.push(link)
                link = link.left_child
                continue
            
            if not stack.is_empty():
                link = stack.pop()
                res.enqueue(link)
                link = link.right_child
                continue
            
            return res

    
    def post_order(self, link):
        res = []

        if link.left_child is not None: # 왼쪽 노드가 있을 경우
            res += self.post_order(link.left_child)  # left recursion
   
        if link.right_child is not None:
            res += self.post_order(link.right_child) # right recursion

        if link is not None:
            res += [link.data] # root 넣어주기

        return res


    def go_left(self, link, before):
        # 왼쪽을 탐색해야하는 경우: 왼쪽 오른쪽 둘다 안했을때
        return link.left_child is not None and \
            link.left_child != before and \
            link.right_child != before
    
    def go_right(self, link, before):
        # 오른쪽을 탐색해야하는 경우: 오른쪽 안했을때
        return link.right_child is not None and \
            link.right_child != before
    


    def post_order_stack(self):
        stack = Stack()
        res = Queue()
        link = self.root
        before = None

        while True:
            if link is not None:
                stack.push(link)

                if self.go_left(link, before): # 왼쪽을 탐색해야하는 경우
                    link = link.left_child
                    continue

                if self.go_right(link, before): # 오른쪽을 탐색해야하는 경우
                    link = link.right_child
                    continue

                
                res.enqueue(link.data)
                if len(res) == self.length: break 

                before = link
                stack.pop() # 현재노드
                link = stack.pop()  # 부모노드 

        return res

    # depth first search
    def bfs(self):
        queue = Queue()
        queue.enqueue(self.root)
        level = 0

        while not queue.is_empty():
            print(f'level{level} : ', end = ' ')
            for i in range(len(queue)):
                node = queue.dequeue()
                print(node.data, end = ' ')       

                if node.left_child is not None:
                    queue.enqueue(node.left_child)

                if node.right_child is not None:
                    queue.enqueue(node.right_child)

            print()
            level += 1    
                

            