def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# 비교 횟수 줄이기
def bubble_sort2(arr):
    for i in range(len(arr) - 1, 0 , -1):
        # 처음에는 len-1, len-2, ,,,,번 비교
        flg = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flg = True
        if not flg: return arr

    return arr

