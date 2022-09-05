def base2_1num(num):
    # 2진법 구하는 거에서 살짝 변형해서, 2진법으로 변경 시 1 개수만 세는 함수
    res = 0

    while num:
        q, r = divmod(num, 2)
        if r == 1:
            res += 1
        num = q
    return res

def solution(n):
    num_of_1 = base2_1num(n)
    
    while True: # 1씩 증가시키며 조건 만족하는 수 찾기
        n += 1
        if base2_1num(n) == num_of_1:
            return n