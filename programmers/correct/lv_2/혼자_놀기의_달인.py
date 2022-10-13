def solution(cards):
    remain = set([i for i in range(len(cards))]) # box 번호들 (cards의 인덱스)
    groups = []
    
    while remain:
        box = list(remain)[0] # 남은 박스 중에 하나 열기
        card = cards[box]
        open_box = []
        while True:
            if box in open_box: # 이미 열었던 박스면 break
                break
            open_box.append(box)
            box = card - 1
            card = cards[box]

        groups.append(open_box) # 이번 회차에 연 박스들 > 하나의 그룹
        remain -= set(open_box)

    if len(groups) == 1: # 그룹이 1개 >> 점수 0점
        return 0

    groups.sort(key = lambda r : len(r), reverse = True)
    return len(groups[0]) * len(groups[1]) # 그룹 중에 가장 많은 박스를 가진 2개 그룹의 박스 수 곱하기