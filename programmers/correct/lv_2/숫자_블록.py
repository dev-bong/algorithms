def solution(begin, end):
    answer = []

    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
            continue
        is_prime = True
        for div_num in range(2, int(i ** 0.5) + 1):
            # root(i)까지 순회하며 가장 작은 약수를 찾기. 단 (i // 약수) <= 10000000 조건을 만족해야함
            q = i // div_num
            r = i % div_num
            if r == 0 and q <= 10000000:
                is_prime = False
                break
        if is_prime: # 소수인 경우 1 넣기
            answer.append(1)
        else: # i // 조건 만족하는 가장 작은 약수
            answer.append(q)

    return answer

"""
n번 위치에는 n의 자기 자신을 제외한 최대 약수 블록이 설치
블록은 10000000번 까지만 있음
"""