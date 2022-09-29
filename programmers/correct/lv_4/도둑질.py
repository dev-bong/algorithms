def solution(money):
    memo = [0] * len(money)
    memo2 = [0] * len(money)

    # 첫번째를 고르는 경우 (마지막은 못고르게 됨)
    memo[0] = money[0]
    memo[1] = money[0]
    for i in range(2, len(money) - 1):
        memo[i] = max([memo[i - 1], memo[i - 2] + money[i]])
    
    # 첫번째 안고르는 경우
    memo2[0] = 0
    memo2[1] = money[1]
    for i in range(2, len(money)):
        memo2[i] = max([memo2[i - 1], memo2[i - 2] + money[i]])
    
    return max([memo[-2], memo2[-1]])

"""
집이 원형이 아니라 선형이라고 가정했을때..
0번째 집부터 시작해서 i번째 집까지 왔을 때 최대값은?
    최대값(i) = max(최대값(i-1), 최대값(i-2) + money(i))
    #? 전자는 i번째 집을 안터는 경우, 후자는 i번째 집을 터는 경우
    
이전 시간초과 풀이에 비해 계산수가 확실히 줄어듬
#* lv3. 스티커 모으기2 와 같은 문제!
"""