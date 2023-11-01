class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    
class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def __len__(self):
        return self.length

    def push(self, data):
        node = Node(data) # 노드 만들고

        if self.top is None:  # top에 아무것도 없으면 top에 노드
            self.top = node
        else:
            node.next = self.top  # top에 있던 애를 node 다음에 이어주기
            self.top = node  # top에 node를
        # length 를 늘리는 코드 필요

    def pop(self):
        if self.top is None: return None
        res = self.top 
        self.top = self.top.next # top의 참조 끊기도록
        return res # top에 있던 애 반환
    
    # top에 있던 data 꺼내보기
    def peek(self):
        if self.top is None : return None
        return self.top.data
    
    # check empty
    def is_empty(self):
        return self.top is None
    
    def __str__(self):
        if self.top is None : return "[]" # 비어있으면
        # 아닐 경우 모든 노드 다 찍어주기
        link = self.top
        res = "[" + str(link.data)
        link = link.next
        while True:
            # 노드 없으면 break
            if link is None : break
            res += ',' + str(link.data)
            link = link.next
        
        res += ' ]'
        return res
