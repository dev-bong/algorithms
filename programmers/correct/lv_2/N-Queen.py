def is_safe(selected, nxt): # 대각선 공격에서 안전한지 체크
    #! 두번째 방법의 is_safe에서 개선
    k = len(selected)
    l = nxt
    for i in range(len(selected)):
        j = selected[i]
        if abs(i - k) == abs(j - l):
            return False
    return True

def n_queen(n, selected, remain): # n_queen 정답 인덱스들을 answer에 저장
    # selected : list, remain : list
    if not remain:
        answer.append(selected)
        return

    for i in range(len(remain)):
        if is_safe(selected, remain[i]): # 다음 퀸은 대각선 공격에서 안전한 곳에 놓기 (가로, 세로 공격은 자동 회피)
            n_queen(n, selected + [remain[i]], remain[:i] + remain[i + 1:])
            # 리스트 끼리 + 한 결과, 슬라이싱한 결과 등을 파라미터로 전달해서 call by reference 처럼 되는 것을 방지

    return

def solution(n):
    global answer
    answer = []

    n_queen(n, [], [i for i in range(n)])
    return len(answer)

"""
n_queen 함수 실행 후 answer에는 정답 인덱스들이 저장됨
    - 예시> answer : [[1, 3, 0, 2], [2, 0, 3, 1]]
    - 퀸은 한 행, 한 열에 하나씩 있어야 하므로 첫번째 답은 [(0, 1), (1, 3), (2, 0), (3, 2)]처럼 읽으면 됨
    #* 가로, 세로 공격은 자동 회피

#! is_safe 개선
    - 원래는 idxs 파라미터 하나만 받아서 해당 인덱스들이 서로서로 대각선 공격에서 안전한가 계산
        >> O(N^2)
    #? 개선 방안 : 원래 idxs에 새로 들어오는 하나에 대해서만 대각선 공격 검사
        >> O(N)
"""

# TODO : 백트래킹? DFS로 풀어보기??