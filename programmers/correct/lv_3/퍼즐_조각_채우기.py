def find(game_board, board_size, v, target):
    """
    board에서의 빈공간 또는 table에서의 퍼즐 조각을 찾는 함수 (퍼즐 형태를 추출)
    BFS 이용
    """
    stack = [v]
    visited = []
    move = [(-1,0), (1,0), (0,-1), (0,1)]
    find_target = {
        "empty" : 0,
        "piece" : 1
    }

    while stack:
        cur_v = stack.pop()
        x, y = cur_v
        
        if cur_v not in visited:
            visited.append(cur_v)
            for mv in move:
                next_x = x + mv[0]
                next_y = y + mv[1]
                if 0 <= next_x < board_size and 0 <= next_y < board_size:
                    if game_board[next_x][next_y] == find_target[target]:
                        stack.append((next_x, next_y))

    return visited

def rotate_90(vertex, board_size):
    """
    주어진 배열을 좌표계로 생각하고 해당 좌표 점을
    일반적인 xy 좌표계 점으로 바꾼 뒤 대칭이동 후 다시 배열 좌표계로..
    """
    i, j = vertex
    if board_size % 2 == 0:
        offset = board_size // 2
        if i < offset:
            y = offset - i
        else:
            y = -(i - offset + 1)
        if j < offset:
            x = j - offset
        else:
            x = j - offset + 1
        rotate_x = y
        rotate_y = -x

        if rotate_x < 0:
            rotate_j = rotate_x + offset
        else:
            rotate_j = rotate_x + offset - 1
        if rotate_y > 0:
            rotate_i = offset - rotate_y
        else:
            rotate_i = offset - rotate_y - 1
        
        return (rotate_i, rotate_j)
    else:
        offset = board_size // 2
        x = j - offset
        y = offset - i
        
        rotate_x = y
        rotate_y = -x

        rotate_i = offset - rotate_y
        rotate_j = rotate_x + offset

        return (rotate_i, rotate_j)

def is_match(shape1, shape2):
    """
    board와 table에서 추출된 모양이 서로 일치하는지 체크
    """
    s1_size = len(shape1)
    s2_size = len(shape2)
    if s1_size == s2_size:
        shape2_rotates = [shape2]
        for i in range(3): # 퍼즐조각을 90도씩 회전해가면서 4가지 버전의 퍼즐조각을 모두 검사
            shape2_rotates.append([rotate_90(o, s2_size) for o in shape2_rotates[i]])

        shape1.sort(key=lambda r:(r[0], r[1])) # 비교 대상인 두 모양 모두 정렬
        for s2 in shape2_rotates:
            s2.sort(key=lambda r:(r[0], r[1]))
            check = set() # 집합을 이용
            for i in range(s2_size):
                check.add((shape1[i][0] - s2[i][0], shape1[i][1] - s2[i][1])) # 정렬 후에는 각 좌표의 차가 모두 같으면 같은 모양임
            if len(check) == 1:
                return True
        return False
    else:
        return False

def solution(game_board, table):
    answer = 0
    size = len(game_board[0])
    board_shapes = []
    visited_board = set()
    table_shapes = []
    visited_table = set()
    filled_board = []

    for i in range(size):
        for j in range(size):
            if game_board[i][j] == 0 and (i,j) not in visited_board:
                res_board = find(game_board, size, (i,j), "empty")
                board_shapes.append(res_board)
                visited_board.update(res_board)
            if table[i][j] == 1 and (i,j) not in visited_table:
                res_table = find(table, size, (i,j), "piece")
                table_shapes.append(res_table)
                visited_table.update(res_table)

    board_empty_spots = len(board_shapes)
    for ts in table_shapes:
        for i in range(board_empty_spots):
            if i not in filled_board and is_match(ts, board_shapes[i]):
                answer += len(ts)
                filled_board.append(i)
                break

    return answer

# TODO : xy 좌표계로 먼저 변환하기. 그러면 rotate_90 함수가 훨씬 간단해질 것으로 보임