def solution(n,a,b):
    a, b = sorted([a, b]) # 작은쪽을 a로
    rounds = 1

    while n // (2 ** rounds) >= 1: # 최종 라운드 까지
        if a % 2 == 1 and (a + 1) == b: # 대결하는 조건 : 붙어있는 홀수, 짝수가 붙게되는데 홀수가 작은 쪽
            break
        a = (a // 2) + (a % 2)
        b = (b // 2) + (b % 2)
        rounds += 1

    return rounds