import random
# 종말의 수
# brute force 
def doom_day(arr, N):
    i = 0
    res = []
    for num in arr:
        if '666' in str(num):
            i += 1
            res.append(num)
            if i == N: return res


arr = [1666, 3636, 5555, 6666, 3666, 79999, 60666]
print(doom_day(arr, 2))
    

def q2(arr):
   for d1 in range(len(arr)-1):
        for d2 in range(d1, len(arr)):
            liars = arr[d1] + arr[d2]
            if sum(arr) - liars == 100:
                a, b = arr[d1], arr[d2]
                arr.remove(a)
                arr.remove(b)
                return arr
                

# test              
arr = [round(random.randrange(10,15)) for _ in range(7)]
t = 100 - sum(arr)
arr[6] = arr[6] + t

arr.append(round(random.randrange(1,20)))
arr.append(round(random.randrange(1,20)))

print(q2(arr))


