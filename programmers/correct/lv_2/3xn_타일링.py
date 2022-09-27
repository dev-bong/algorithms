def solution(n):
    if n % 2 == 1: # 홀수
        return 0
    
    n3 = [0 for i in range(n + 1)]

    n3[0] = 1
    n3[2] = 3

    for i in range(4, n + 1, 2):
        n3[i] = (3 * n3[i - 2] + 2 + sum([n3[i - j] * 2 for j in range(4, i - 1, 2)])) % 1000000007
    
    return n3[n] % 1000000007

"""
#* 2xn 타일링 문제랑 연계되는 문제..
점화식만 잘 세우면 됨

일단 이 경우는 짝수만 됨
    A(n)
        1. 처음 두칸을 채우는 경우 : 3 * A(n - 2)
            - 두칸을 채우는 경우의 수 = 3
        2. 아래 링크 참조..
#! 점화식 이해 좀더 하도록 : https://dev-note-97.tistory.com/182
"""