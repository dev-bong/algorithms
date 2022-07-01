def max_p(p): # 최대 중요도
    if not p:
        return -1
    p_list = [_[1] for _ in p]
    return max(p_list)

def solution(priorities, location):
    answer = 0
    idx_pr = [(i, priorities[i]) for i in range(len(priorities))] # (인덱스, 중요도) 튜플 리스트 생성
    print(idx_pr)

    while idx_pr:
        m = max_p(idx_pr[1:])
        if idx_pr[0][1] < m:
            idx_pr = idx_pr[1:] + [idx_pr[0]]
        else:
            answer += 1
            dq_item = idx_pr[0]
            idx_pr = idx_pr[1:]
            if dq_item[0] == location:
                return answer