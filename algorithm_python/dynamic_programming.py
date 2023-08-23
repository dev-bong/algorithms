global cnt1, cnt2, memo
cnt1 = 0
cnt2 = 0
memo = {
    0 : 1,
    1 : 1
}

def fibo(n): # 그냥 재귀 피보나치
    global cnt1
    cnt1 += 1
    if n in [0, 1]:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

def fibo_memo(n): # 동적계획법 피보나치
    global cnt2, memo
    cnt2 += 1
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibo_memo(n - 1) + fibo_memo(n - 2)
        return memo[n]

n = 10
print(fibo(n), fibo_memo(n))
print("fibo cnt :", cnt1)
print("fibo_memo cnt :", cnt2)