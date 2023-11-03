
# 분할 정복 문제 : 거듭제곱 최적화
# O(2**log2N)
def power(a,b):
    if b == 0: return 1
    if b == 1: return a

    if b%2 == 0:
        return power(a,b//2) * power(a, b//2)
    else:
        return power(a,b//2) * power(a,b//2) * a
    
print(power(2,5))


# O(log2b)
def power2(a,b):
    if b == 0: return 1
    result = power2(a, b//2)

    if b % 2: # 홀수
        return result * result * a
    else:
        return result * result



        