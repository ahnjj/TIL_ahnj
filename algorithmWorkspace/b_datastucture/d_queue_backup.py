class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def __len__(self):
        return self.length
    
    # 뒤에 넣어주는
    def enqueue(self, data):
        node = Node(data)
        if self.front is None:  # 빈 큐일때
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        
        self.length += 1

    # 꺼내는 것
    def dequeue(self):
        node = self.front
        if node is None: return None  # 빈 큐일때

        if node == self.rear:  # 맨 끝 노드일때
            self.front = None # 앞뒤 둘다 참조 끊어줌
            self.rear = None
        else:
            self.front = self.front.next
        
        self.length -= 1
        return node.data
    
    def is_empty(self):
        return self.front is None
    
    def __str__(self):
        if self.front is None : return "[]" # 비어있으면
        # 아닐 경우 모든 노드 다 찍어주기
        link = self.front
        res = "[" + str(link.data)
        link = link.next
        while True:
            # 노드 없으면 break
            if link is None : break
            res += ',' + str(link.data)
            link = link.next
        
        res += "]"
        return res




