def find_square(i, j, board, i_len, j_len):
    size = 1

    while True:
        i_side = True
        j_side = True

        if (i + size) >= i_len or (j + size) >= j_len:
            break

        for l in range(j, j + size + 1):
            if board[i + size][l] != 1:
                i_side = False
                break
        
        for l in range(i, i + size + 1):
            if board[l][j + size] != 1:
                j_side = False
                break

        if i_side and j_side:
            size += 1
        else:
            break

    return size

def solution(board):
    answer = 0
    i_len = len(board)
    j_len = len(board[0])
    global visited

    for i in range(i_len):
        for j in range(j_len):
            if board[i][j] == 1:
                answer = max([answer, find_square(i, j, board, i_len, j_len)])

    return answer ** 2

# TODO : DP로 다시 풀어보기