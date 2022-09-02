def solution(land):
    row_size = len(land[0])
    col_size = len(land)
    dp = [[0, 0, 0, 0] for i in range(col_size)]
    idxs = set([0, 1, 2, 3])

    for i in range(row_size):
        dp[0][i] = land[0][i]
    
    for i in range(1, col_size):
        for j in range(row_size):
            cand = []
            for k in (idxs - {j}): # 같은 라인 칸은 빼고 밟기
                cand.append(dp[i - 1][k])
            dp[i][j] = land[i][j] + max(cand)
    
    return max(dp[col_size - 1])