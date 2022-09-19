
#! 첫번째 방법 : 전체 경우의 수? - 대각선 공격
#! 테스트 케이스 10, 11 시간 초과. permutations로 경우의 수 구하는게 너무 많은 것 같다

from itertools import permutations

def is_safe(idxs): # 대각선 공격에서 안전한지 체크
    for i in range(len(idxs)):
        j = idxs[i]
        for k in range(len(idxs)):
            if i == k:
                continue
            l = idxs[k]

            if abs(i - k) == abs(j - l): # 대각선에 있는 조건
                return False
    return True

def solution(n):
    answer = []
    idxs = [i for i in range(n)] # queen은 한 행, 한 열에 하나씩만 들어갈 수 있으므로 각 행에서 몇번째 인덱스에 있는지를 표시
    cases = permutations(idxs, n) # 대각선 공격은 제외하고 queen을 배치할 수 있는 모든 경우의 수

    for case in cases:
        if is_safe(case):
            answer.append(case)

    return len(answer)


#! 두번째 방법 : 나름대로 재귀
#! 테스트 케이스 11 시간 초과 (방법 1보다는 개선). is_safe를 비교하는 수가 너무 많은 듯 하다

def is_safe(idxs): # 대각선 공격에서 안전한지 체크
    for i in range(len(idxs)):
        j = idxs[i]
        for k in range(len(idxs)):
            if i == k:
                continue
            l = idxs[k]

            if abs(i - k) == abs(j - l): # 대각선에 있는 조건
                return False
    return True

def n_queen(n, selected, remain): # selected : list, remain : list
    if not remain:
        answer.append(selected)
        return

    for i in range(len(remain)):
        if is_safe(selected + [remain[i]]):
            n_queen(n, selected + [remain[i]], remain[:i] + remain[i + 1:])

def solution(n):
    global answer
    answer = []

    n_queen(n, [], [i for i in range(n)])
    
    return len(answer)