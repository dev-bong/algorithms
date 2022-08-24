def steal(money, house_num, idxs):
    # idxs : 훔친 집의 인덱스들?? set?
    global max_memo, idx_memo

    next_idxs = set()
    for i in range(house_num):
        if (i % house_num) not in idxs and ((i - 1) % house_num) not in idxs and ((i + 1) % house_num) not in idxs:
            # 이미 털었던 집, 털었던 집과 인접한 집은 털 수 없음
            next_idxs.add(i)

    if next_idxs: # 다음에 털 집이 있으면..
        for next_idx in next_idxs:
            tmp = idxs | {next_idx}
            if tmp not in idx_memo: # 털 집의 집합들이 계산 안해본 것일 때만 콜 (재귀함수 콜 줄이기)
                steal(money, house_num, tmp)
                idx_memo.append(tmp)
            else:
                pass
    else: # 다음에 털집 없으면
        total_money = 0
        for idx in idxs:
            total_money += money[idx]
        max_memo = max([max_memo, total_money])

def solution(money):
    global max_memo, idx_memo
    max_memo = 0
    idx_memo = []

    steal(money, len(money), set())

    return max_memo

"""
모든 케이스에서 시간초과 발생
- 아래 테스트 케이스는 모두 맞춤..
- 시간제한이 좀 빡빡한 것 같음
"""

# 테스트케이스
print(solution([1,2,3,1]), 4)
print(solution([1,1,4,1,4]), 8)
print(solution([1000,0,0,1000,0,0,1000,0,0,1000]), 3000)
print(solution([1000,1,0,1,2,1000,0]), 2001)
print(solution([1000,0,0,0,0,1000,0,0,0,0,0,1000]), 2000)
print(solution([1,2,3,4,5,6,7,8,9,10]), 30)
print(solution([0,0,0,0,100,0,0,100,0,0,1,1]), 201)
print(solution([11,0,2,5,100,100,85,1]), 198)
print(solution([1,2,3]), 3)
print(solution([91,90,5,7,5,7]), 104)
print(solution([90,0,0,95,1,1]), 185)
print(solution([0, 0, 0, 100, 0, 0]), 100)