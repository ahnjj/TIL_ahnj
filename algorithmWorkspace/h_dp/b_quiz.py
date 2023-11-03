# dp
def q1(arr):
    cur = 0
    before = [0]

    for i in arr:
        cur += i
        if cur < min(before):
            cur = 0
        before.append(cur)
    return max(before)
        
def q2(arr):
    sum_arr = [arr[0]]

    for e in arr[1:]:
        sum_arr.append(max(sum_arr[-1]+e, e))
    return max(sum_arr)


print(q1([10, -4, 3, 1, 5, 6, -35, 12, 21, -1]))
print(q2([10, -4, 3, 1, 5, 6, -35, 12, 21, -1]))