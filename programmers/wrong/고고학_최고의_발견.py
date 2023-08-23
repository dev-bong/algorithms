def around_check(i, j, board, size): # (i, j) 인접한 칸에 0이 있나없나 체크
    edge = [-1, size]
    around = [board[i][j]]

    i_around = set([i - 1, i + 1]) - set(edge)
    j_around = set([j - 1, j + 1]) - set(edge)
    for ia in i_around:
        around.append(board[ia][j])
    for ja in j_around:
        around.append(board[i][ja])

    return True if 0 not in around else False # 인접한 칸에 0 없으면 true

def around_turn(i, j, board, size): # (i, j) 인접한 칸 시계방향 돌리기
    edge = [-1, size]

    i_around = set([i - 1, i + 1]) - set(edge)
    j_around = set([j - 1, j + 1]) - set(edge)
    board[i][j] = (board[i][j] + 1) % 4

    for ia in i_around:
        board[ia][j] = (board[ia][j] + 1) % 4
    for ja in j_around:
        board[i][ja] = (board[i][ja] + 1) % 4

def solve_puzzle(clockHands, size):
    for i in range(size):
        for j in range(size):
            if around_check(i, j, clockHands, size):
                around_turn(i, j, clockHands, size)
                return 0
    return -1

def solution(clockHands):
    answer = 0
    size = len(clockHands)

    while solve_puzzle(clockHands, size) != -1:
        answer += 1
        print(clockHands)
    return answer