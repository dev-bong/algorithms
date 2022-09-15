def solution(n, left, right):
    answer = []

    for index in range(left, right + 1): # right - left 만큼만 반복하면 됨
        i = index // n
        j = index % n
        answer.append(max([i, j]) + 1)
        
    return answer


#! 아래는 시간 초과 풀이
def solution(n, left, right):
    answer = []
    board = [[0] * n for i in range(n)]

    # 여기서 O(N^2)
    for i in range(n):
        for j in range(n):
            bigger = max([i, j])
            board[i][j] = bigger + 1 # 규칙성 찾아낸것
    
    # O(N)
    for b in board:
        answer.extend(b)

    return answer[left:right+1] # 슬라이싱도 시간복잡도가 꽤 됨