# [1,5,7,13] [2,4,9,12,15]
# 이미 정렬이 된 두 배열 합체
from datastructure.d_queue import Queue

# 두 배열을 merge하는 함수
def merge(arr1, arr2):
    res = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    # arr1 배열에 남은 원소들이 있으면 다 넣어준다.
    if i < len(arr1):
        res += arr1[i:len(arr1)]
    else:
        res += arr2[j:len(arr2)]
    
    return res

# merge sort 함수
def mergesort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    # arr를 2개로 분할한다.
    mid = n // 2
    arr1 = mergesort(arr[0:mid]) # recursion
    arr2 = mergesort(arr[0:mid])
    return merge(arr1, arr2) # merge 2 arrays


# recursion없이 queue로
def mergesort2(arr):
    n = len(arr)
    if n <= 1:
        return arr
    queue = Queue()
    for e in arr:
        queue.enqueue([e])  # 분할 할 필요 없이 하나씩 다 쪼개져서 들어옴 (list로 넣어야 합병이 가능)
    
    # 2개씩 꺼내서 merge하고 queue 뒤에 넣어주기
    while len(queue) > 1:
        arr1 = queue.dequeue() # 첫번째 요소 
        arr2 = queue.dequeue() # 두번째 요소
        queue.enqueue(merge(arr1, arr2)) # 합쳐진 배열이 queue에
    
    return queue.dequeue()
    

        


