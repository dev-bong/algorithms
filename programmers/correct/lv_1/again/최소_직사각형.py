def solution(sizes):
    answer_w = max([max(size) for size in sizes]) # 변 중에 제일 큰거는 무조건 하나 포함
    answer_h = 0
    h_candidate = []

    for size in sizes: # 명함의 작은 변중에 제일 큰거 선택
        size.sort()
        mn, mx = size
        h_candidate.append(mn)
    
    answer_h = max(h_candidate)

    return answer_w * answer_h