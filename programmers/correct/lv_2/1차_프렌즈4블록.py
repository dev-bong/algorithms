def solution(m, n, board):
    answer = 0

    for i in range(len(board)): # board 2차원 배열 형태로 세팅
        board[i] = list(board[i])

    while True:
        pang = set()
        for i in range(len(board) - 1):
            for j in range(len(board[0]) - 1):
                if (board[i][j] != "X" # 빈 칸이 아니고
                and board[i][j] == board[i][j + 1] # (i, j)부터 우하단 대각선 방향으로 2X2 가 모두 같으면
                and board[i][j] == board[i + 1][j]
                and board[i][j] == board[i + 1][j + 1]):
                    pang.update([(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)]) # 팡!

        if not pang: # 팡!이 없으면 break
            break

        answer += len(pang)
        for p in pang: # 이번 회차 팡! 한번에 수행
            i, j = p
            board[i][j] = "X"

        for i in range(1, len(board)): # 빈칸 위에 있는 블록들 떨어지는 로직
            for j in range(len(board[0])):
                if board[i][j] == "X": # 빈칸이면 (i, j)부터 위에서 땡겨오면서 끝까지 올라가기
                    for k in range(i, 0, -1):
                        board[k][j] = board[k - 1][j]
                        board[k - 1][j] = "X"

    return answer