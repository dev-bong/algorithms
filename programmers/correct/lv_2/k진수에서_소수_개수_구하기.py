def n_base_num(num, n): # n 진수로 변환
    res = ""
    while True:
        q = num // n
        r = num % n
        if q < 1:
            res += str(r)
            break
        res += str(r)
        num = q
    return res[::-1]

def is_prime(num): # 소수 판별
    if num == 1:
        return False
        
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    k_base = n_base_num(n, k)
    p_list = k_base.split("0") # p 추출

    for p in p_list:
        if p:
            if is_prime(int(p)):
                answer += 1
    
    return answer