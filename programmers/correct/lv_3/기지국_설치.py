def solution(n, stations, w):
    answer = 0
    border = []

    # 전파가 닿지 않는 구간 나누기
    border.append(1)
    for station in stations:
        border.append(station - (w + 1))
        border.append(station + w + 1)
    border.append(n)

    # 각 구간마다 최소 기지국으로 커버
    for i in range(0, len(border), 2):
        print(border[i], border[i + 1])
        if border[i] > border[i + 1]:
            continue
        gap = border[i + 1] - border[i] + 1
        q, r = divmod(gap, 2 * w + 1) # 최대 커버 범위로 설치하고, 남은 곳에도 설치 (나머지 있을 경우)

        answer += q + 1 if r else q

    return answer

"""
전파가 닿지 않는 곳을 채우는 문제

어떤 곳에 기지국을 설치할 경우 양쪽으로 w만큼 전파 커버
    >> 최대 2*w + 1 만큼 전파 커버 가능
"""