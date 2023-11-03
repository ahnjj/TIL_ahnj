# 피보나치 수열을 dp로 구현했을 때
def fibo_dp(n):
    table = []
    table += [1,1]

    if n < 1: return -1
    if n < 2:
        return table[-1]
    
    for i in range(2, n+1):
        table.append(table[i-2] + table[i-1])
    
    return table[-1]

print(fibo_dp(10))