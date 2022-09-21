def solution(board):
    dp = [[0 for i in range(len(board[0]))] for j in range(len(board))]
    dp[0] = board[0][:]

    for i in range(1, len(board)):
        dp[i][0] = board[i][0]
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                if dp[i - 1][j - 1] > 0:
                    if dp[i - 1][j - 1] <= dp[i - 1][j] and dp[i - 1][j - 1] <= dp[i][j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = min([dp[i - 1][j], dp[i][j - 1]]) + 1
                else:
                    dp[i][j] = 1
    
    return max([max(dp[i]) for i in range(len(dp))]) ** 2

"""
dp[i][j] : (i, j)를 끝으로 하는 최대크기 정사각형 (정사각형은 좌상단에서 우하단으로)
"""