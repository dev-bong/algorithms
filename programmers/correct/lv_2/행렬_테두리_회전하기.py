def do_query(arr, query):
    change_idxs = []
    change_values = []
    x1, y1 = sorted([query[0] - 1, query[2] - 1]) # x1 < y1, x2 < y2가 되도록 설정
    x2, y2 = sorted([query[1] - 1, query[3] - 1])

    # (x1, x2)부터 시계방향으로 돌며 수집
    for i in range(x2, y2 + 1): # 좌상단(x1, x2) -> 우상단(x1, y2)
        change_idxs.append((x1, i))
        change_values.append(arr[x1][i])
    for i in range(x1 + 1, y1 + 1): # 우상단(x1, y2) -> 우하단(y1, y2)
        change_idxs.append((i, y2))
        change_values.append(arr[i][y2])
    for i in range(y2 - 1, x2 - 1, -1): # 우하단(y1, y2) -> 좌하단(y1, x2)
        change_idxs.append((y1, i))
        change_values.append(arr[y1][i])
    for i in range(y1 - 1, x1, -1): # 좌하단(y1, x2) -> 좌상단(x1, x2)
        change_idxs.append((i, x2))
        change_values.append(arr[i][x2])

    for i in range(len(change_idxs)):
        x, y = change_idxs[i]
        arr[x][y] = change_values[i - 1] # 한칸씩 밀어서 값 바꾸기

    return min(change_values)

def solution(rows, columns, queries):
    answer = []
    arr = []

    num = 1
    for i in range(rows):
        tmp = []
        for j in range(columns):
            tmp.append(num)
            num += 1
        arr.append(tmp)

    for query in queries:
        min_val = do_query(arr, query)
        answer.append(min_val)
    
    return answer

# TODO : deque에 rotate 이용?