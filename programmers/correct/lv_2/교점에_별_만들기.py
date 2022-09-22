def is_int(num):
    return True if num - int(num) == 0 else False

def solution(line):
    answer = []
    points = []

    while line:
        cur = line.pop()
        for l in line: # 라인끼리 비교해 가면서 문제에 나온 공식에 의거해서 교점 찾기
            a, b, e = cur
            c, d, f = l

            m = (a * d) - (b * c)
            if m == 0:
                continue
            x = ((b * f) - (e * d)) / m
            y = ((e * c) - (a * f)) / m

            if is_int(x) and is_int(y): # 정수 교점만 인정
                points.append((int(x), int(y)))

    if len(points) == 1: # 교점이 1개일 경우
        return ["*"]

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    xs.sort()
    ys.sort()

    # 표현하는 격자판을 위해 x 최소, 최대값, y 최소, 최대값 구하기
    min_x, max_x, min_y, max_y = [xs[0], xs[-1], ys[0], ys[-1]]
    
    # 격자판 그리기
    for y in range(max_y, min_y - 1, -1): # y 좌표는 큰곳 ~ 작은곳
        tmp = ""
        for x in range(min_x, max_x + 1): # x 좌표는 작은곳 ~ 큰곳
            if (x, y) in points:
                tmp += "*" # 교점이면 별찍기
            else:
                tmp += "."
        answer.append(tmp)
    return answer