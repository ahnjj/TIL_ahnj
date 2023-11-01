from b_hashtable import HashTable


def q1_me(text):
    hashtable = HashTable()
   
    for c in text:
    # 1. key-value형식으로 해쉬테이블에 문자 넣기
        if hashtable.__contains__(c):
            data = hashtable.get(c)
            hashtable.set(c, data+1)
        else:
            hashtable.add(c, 1)

    length = hashtable.table_length


    #2. max
    hash_max = 1
    res = set()
    # 왜 바로 value값이 나오지
    for i in hashtable:
        if i > hash_max:
            hash_max = i  # 그 키의 value값
    # key는 어떻게 접근하지 (data.key)

    # 3. max 여러개 있을 때 고려
    for c in text:
        # index = hash(c)
        if hashtable.get(c) == hash_max:
            res.add(c)

    return list(res)

def q1(text:str):
    hashtable = HashTable()

    for ch in text:
        if ch not in hashtable: # 이미 그 ch가 있으면
            hashtable.add(ch, 1)
        else:
            hashtable.set(ch, hashtable.get(ch)+1)  # 이미 있으면 data값 1 증가

    # max값 찾기
    res = []
    max = 1

    # value값을 돌면서 최대 value값을 찾는다.
    for e in hashtable:
        if max < e.data : max = e.data

    for e in hashtable:
        if max == e.data :
            res.append(e.key)   # 그때 data.key로 해서 key값에 접근한다.
    
    return res
    
    
    
    