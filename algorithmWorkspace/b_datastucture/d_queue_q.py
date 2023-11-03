from b_datastucture.d_queue import Queue
def q1(num):
    # 1.queue 만들기
    cards = Queue()
    for i in range(1, num+1):
        cards.enqueue(i)
    
    # 2. 반복
    res = []
    for i in range(num-1):  # while len(cards) > 1:
        # 위에있는 거 빼기
        res.append(cards.dequeue())
        # 그 다음 위에 있는거 빼서 뒤에 넣기
        cards.enqueue(cards.dequeue())

    # 마지막 한장
    res.append(cards.dequeue())
    return res
    
# 요세푸스 순열 문제
def q2(num, k):
    # 1.queue 만들기
    queue = Queue()
    for i in range(1, num+1):
        queue.enqueue(i)
    res = []

    # 원소 개수만큼 반복
    for i in range(num):
        # 2. k-1번 front를 빼서 뒤에 넣기
        for j in range(k-1):
            next = queue.dequeue()
            queue.enqueue(next)
        
        # 3. k번째 애를 제거하기
        turn = queue.dequeue()
        res.append(turn)

    return res



