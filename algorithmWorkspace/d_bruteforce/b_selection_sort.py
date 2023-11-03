def selection_sort(arr):
    # pointer 1개
    for p in range(len(arr)-1):
        min = p
        # 나머지 배열 최소값 찾기
        for i in range(p, len(arr)):
            if arr[min] > arr[i]:
                min = i
        arr[p], arr[min] = arr[min], arr[p]
    return arr

