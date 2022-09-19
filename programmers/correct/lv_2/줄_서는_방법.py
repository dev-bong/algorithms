def solution(n, k):
    answer = []
    humans = [i for i in range(1, n + 1)] # 1 ~ n 까지 사람들 (자연스럽게 정렬도)
    fact = [1 for i in range(n)]

    for i in range(2, n): # 1! ~ (n-1)! 까지 구하기
        fact[i] = i * fact[i - 1]

    i = 1
    while True: # 앞에서부터 한자리 씩 구하기
        q =  k // fact[n - i]
        k = k % fact[n - i]

        answer.append(humans[q])
        del humans[q]

        if k == 1: # 나머지가 1 : 완성된 부분 제외 나머지로 사전식 배열 중 1빠따
            answer.extend(humans)
            break
        if k == 0: # 나머지가 0 : 완성된 부분 제외 나머지로 사전식 배열 중 마지막 빠따
            humans.sort(reverse=True)
            answer.extend(humans)
            break
        i += 1

    return answer

"""
1부터 n까지 숫자를 나열한 것 중 사전순으로 k번째인 수를 찾는 문제

#? 첫자리 구하는 예시
    1 로 시작 : (n - 1)!
    2 로 시작 : (n - 1)!
    ...
    n 로 시작 : (n - 1)!

    >> 이런식으로 되어있기 때문에 k를 (n - 1)!으로 나눠서 무엇으로 시작하는지 체크 가능
"""