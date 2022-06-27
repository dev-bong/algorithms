def solution(board, moves):
    answer = 0 # 터져서 없어진 인형 수
    board_len = len(board[0])
    stacks = [[] for i in range(board_len)] #? [[]*board_len]
    buckets = []

    for i in range(board_len): # 보드 상태를 스택 배열로 변환. 각 스택은 각 라인을 나타냄.
        for j in range(board_len-1, -1, -1):
            if board[j][i] == 0:
                continue
            stacks[i].append(board[j][i])

    for mv in moves:
        move = mv - 1
        if stacks[move]: # 해당 라인에 인형이 있으면 pop
            pop_doll = stacks[move].pop()
        else: # 없으면 무시
            continue

        if buckets:
            if buckets[-1] == pop_doll: # 이전 인형과 같으면 터져서 없어짐
                buckets.pop()
                answer += 2 # 없어지는건 2개씩
            else:
                buckets.append(pop_doll) # 이전 인형과 다르면 바구니에 그냥 쌓기
        else:
            buckets.append(pop_doll)

    return answer