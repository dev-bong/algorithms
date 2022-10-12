def solution(lines):
    line_set = []
    answer = set()
    for line in lines:
        line.sort()
        line_set.append(set([i for i in range(line[0], line[1])]))

    # 각 선분끼리 겹치는 선분 구하기
    u1 = line_set[0] & line_set[1]
    u2 = line_set[0] & line_set[2]
    u3 = line_set[1] & line_set[2]

    # 겹치는 선분들 중 겹치는 부분이 있으면 합치기
    for u in [u1, u2, u3]:
        answer |= u

    return len(answer)