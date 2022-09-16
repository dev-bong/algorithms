def check(board): # board가 쿼드압축 가능한지(안의 값이 모두 같은지) 체크 후 같다면 그 값을 출력
    if len(board) == 1: # board가 한칸짜리일 경우
        return board[0][0]

    value = board[0][0]

    for i in range(len(board)):
        for j in range(len(board)):
            if value ^ board[i][j] == 1: # ^는 xor. xor를 이용해서 서로 다른지 체크 (0 또는 1이라서 이렇게 함)
                return -1
            value = board[i][j]
    return value

def divide(board): # board를 작은 정사각형으로 4등분
    p1, p2, p3, p4 = [[], [], [], []]
    for i in range(len(board)//2):
        p1.append(board[i][:len(board)//2])
        p2.append(board[i][len(board)//2:])
    for i in range(len(board)//2, len(board)):
        p3.append(board[i][:len(board)//2])
        p4.append(board[i][len(board)//2:])
    return [p1, p2, p3, p4]

def solution(arr): # arr는 정사각형 모양. 한변 길이는 2의 제곱수
    answer = [0, 0]
    zips = [] # 압축 완료된 값
    remain = [arr]

    while remain:
        piece = remain.pop()

        zip_res = check(piece)
        if zip_res != -1: # 해당 조각이 쿼드 압축 가능
            zips.append(zip_res)
        else:   # 압축 조건 안됨. 4개로 쪼개기
            remain.extend(divide(piece)) # 쪼갠 조각 remain에 push
    
    for z in zips:
        answer[z] += 1
    return answer