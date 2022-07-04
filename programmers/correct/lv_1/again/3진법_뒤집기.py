def N_base_num(num, N): # 특정 수 N진법으로 변환 (문자열 리턴)
    res = ""
    
    while True:
        q = num // N
        r = num % N
        if q == 0:
            res += str(r)
            break
        num = q
        res += str(r)
    return "".join(reversed(list(res))) # res[::-1] 문자열 또는 리스트 뒤집는 방법?

#? int(number, 3) ??? divmod??

def solution(n):
    answer = 0
    n_3base = N_base_num(n, 3)

    for i in range(len(n_3base)): # 3진법 수를 거꾸로해서 10진법
        answer += int(n_3base[i]) * (3 ** i)
    return answer