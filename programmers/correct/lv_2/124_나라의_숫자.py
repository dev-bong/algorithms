def solution(n):
    answer = ''

    while n:
        q = n // 3
        r = n % 3

        if r == 0:
            q -= 1
            r = 4

        answer += str(r)

        n = q

    return answer[::-1]

"""
숫자 3개로 수를 표현
    - 3진법 관련 문제
    - 다만 0, 1, 2가 아닌 1, 2, 4를 사용

    - 124나라 방법에서는 나머지가 0일 때, 자릿수가 올라가지 않고 몫 - 1, 나머지는 4로 표현
        ex> #! 4는 3진법에서 10과 같음
            6 >> 14
            7 >> 21
            8 >> 22
            9 >> 24 : 2는 2, 4는 10
                #* 20 + 10 = 100
            10 >> 41
                #* 100 + 1
"""