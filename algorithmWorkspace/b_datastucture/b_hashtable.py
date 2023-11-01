class Node:
    def __init__(self, key:str, data):
        self.key = key
        self.data = data
        self.next = None

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return 31 * sum([ord(s) for s in self.key]) # aaabb [97,97,97,98,98]
         # hash table에서 중복된 해시값을 피하기 위해 31 곱해줌
    
    def __str__(self):
        return "{key=" + self.key + ", data=" + str(self.data) + "}"
        # return "{key=" + self.key + ", data=" + self.data + "}"

class DuplicateKey(RuntimeError): pass  # 예외 객체(runtime에러 상속)
        

class HashTable:
    # initialize hash table
    def __init__(self, length = 4):
        self.table_length = length
        self.table = [None for _ in range(self.table_length)]  # [None] * self.table_length와 같음
        self.length = 0 # 실제 사이즈

    # Takes a key and returns an index in the array
    # self.table의 어떤 인덱스에 저장할지 결정하기 위한 해시함수
    def hash(self, node):  # key를 매개변수로 받음
        # print(hash(node) % self.table_length)
        return hash(node) % self.table_length  # python built-in hash function


    # add, set 부분 로직만 따로(변경되어야하는 부분을 함수로)
    def __add(self, link, node):
        if(link == node): 
            raise DuplicateKey

    def __set(self, link, node):
        if(link == node):
            link.data = node.data
            raise DuplicateKey

   

    # 외부에서 붙이지 말라는(private)의미로 __붙임
    def __add_context(self, key:str, data, callback_fn):
        if type(key) is not str:
            raise TypeError("key가 str이 아님")
        
        node = Node(key, data)
        index = self.hash(node)

        if self.table[index] is None:
            self.table[index] = node
        else:
            link = self.table[index]

            while(True):
                # if(link == node): return # 이 부분을 모듈화.
                try:
                    callback_fn(link, node)
                except:
                    return      # exception 하면 함수 종료됨  
                if(link.next is None):
                    link.next = node
                    break

                link = link.next
        
        self.length += 1

    
    # 데이터를 추가, 만약 같은 기가 존재할 경우 데이터를 덮어쓰지 않음
    def add(self, key:str, data):
        self.__add_context(key, data, self.__add)

    
    # 데이터를 추가 및 수정, 같은 키가 존재하면 데이터를 덮어씀 (setter)
    def set(self, key:str, data):
       self.__add_context(key, data, self.__set)


    def __str__(self):
        # ['{key=d, data=안녕하세요}','{key=...}']로 변경해보기
        # res = ''

        # for i in range(len(self.table)):
        #     head = self.table[i]
        #     res += 'key='+head.key+', '+ 'data= ' +head.data+'\n'
    
        #     while head.next:
        #         head = head.next
        #         res += 'key='+head.key+', '+ 'data= ' +head.data+'\n'

        # return res

        res = []

        for link in self.table:
            if link is None: continue

            while True:
                res.append(str(link))
  
                if link.next is None :
                    break
                link = link.next       
        return str(res)

    # 노드 전체 탐색
    # 해당 key의 인덱스에 있는 노드
    def get(self, key: str):
        if type(key) is not str:
            raise TypeError("key가 str이 아님")
        node = Node(key, None)
        index = self.hash(node)
        link = self.table[index]

        if link is None : return None # 빈 노드이면 넌 반환
        if link == node : return link.data # 들어온 노드가 테이블 첫번째 노드일때 value반환
        link = link.next

        while(True):
            if link is None : break # 빈 노드이면 넌 반환
            if link == node : return link.data 
            link = link.next

        return None
    
    # 해당 키의 노드 제거
    def remove(self, key:str):
        if type(key) is not str:
            raise TypeError('Key가 str이 아님')
        
        # 해당 키의 value값이 None인 노드 만들고
        node = Node(key, None)
        idx = self.hash(node)   # 인덱스(해싱된 값)뽑아내기 (내장 함수hash호출하면 안되고 만든 함수 self.hash호출해야함)

        # 해당 인덱스로 접근해서 해당 chain 탐색
        link = self.table[idx]
        if self.table[idx] is None: return # 없는 노드일때

        # head가 해당 노드일때
        if link == node:  
            self.table[idx] = self.table[idx].next
            self.length -= 1 # length 하나 줄여주기(node제거 했으니까)
            return 

        prev = link
        link = link.next

        while True:
            if link is None:  # 끝까지 탐색했는데도 없으면 리턴
                return
            # link 랑 node랑 비교
            if link == node: 
                prev.next = link.next
                self.length -= 1
                return None
            prev = link
            link = link.next  # 다음으로 넘어감

        return None


    
    # 해시테이블에 해당 key가 있는지 검사
    def __contains__(self, key:str):
        if type(key) is not str:
            raise TypeError('key가 str이 아님')
        
        return True if self.get(key) is not None else False
    

    def __iter__(self):
        return HashTable.Iterator(self)
        
    class Iterator:
        def __init__(self, hashtable):
            self.table = hashtable.table
            self.size = hashtable.length
            self.p1 = 0   # table인덱스 탐색 포인터
            # self.p2 = 0   # 필요없음
            self.iter_cnt = 0
            self.node = self.table[self.p1]

        def __iter__(self):
            return self
        
        def __next__(self):
           
            if self.iter_cnt >= self.size:
                raise StopIteration

            # 비어있는애 있으면 테이블 다음 인덱스로 넘어가기
            while self.table[self.p1] is None:
                self.p1 += 1
            
            # 이전 iter에서 테이블 한 인덱스 노드에서 맨끝에 다달았을때
            # 다음 테이블 인덱스로 넘어간다.
            if self.node is None:
                self.node = self.table[self.p1] 
                
            if self.node.next is None:
                self.p1 += 1 # 바깥 테이블 인덱스 1 증가
          
            res = self.node.data

            self.iter_cnt += 1
            self.node = self.node.next  # 연결 노드 다음 노드로

            return res
        

