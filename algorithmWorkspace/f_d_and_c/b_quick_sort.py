# 배열을 둘로 만드는 함수
from datastructure.c_stack import Stack


def partition(arr, low, high):
    pivot = arr[low] # 맨 앞 원소가 피봇
    j = low
   
    # pivot 보다 큰 것음 뒤에, 작은 것은 앞에
    for i in range(low + 1, high + 1):
        if arr[i] < pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
        print(arr,pivot)
    
    pivot = j
    arr[low], arr[pivot] = arr[pivot], arr[low]
    return pivot

# quicksort함수
def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot-1)
        quicksort(arr, pivot+1, high)

    return arr


# stack으로 구현
def quicksort_stack(arr):
    stack = Stack()
    stack.push([0, len(arr)-1])
 
    while not stack.is_empty():
        tmp = stack.pop()
        low = tmp[0]
        high = tmp[1]

        if low < high:
            pivot = partition(arr, low, high)
            stack.push([low, pivot - 1])
            stack.push([pivot + 1, high])

    return arr