from itertools import combinations

def solution(numbers):
    answer = []
    cases = combinations(numbers, 2)
    
    for case in cases:
        answer.append(sum(case))
    answer = list(set(answer))
    answer.sort()
    return answer

# TODO : combinations 안쓰고 해보자