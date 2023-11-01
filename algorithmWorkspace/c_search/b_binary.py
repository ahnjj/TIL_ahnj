# 이진탐색
# 데이터가 오름차순, 내림차순으로 정렬되어 있다는 전제 하에 검색

def bin_search(arr, key):
    pl = 0
    pr = len(arr) - 1

    while pl <= pr:
        center = (pl + pr) // 2

        if arr[center] == key: return center
        elif key > arr[center]:
            pl = center + 1
        else:
            pr = center - 1

    return -1 # 다 찾았는데도 없으면

print(bin_search(sorted([5,2,6,78,1,34,45]),5))

