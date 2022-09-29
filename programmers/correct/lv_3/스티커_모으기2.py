def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
        
    dp = [0] * len(sticker)
    dp2 = [0] * len(sticker)

    # 첫번째 스티커 떼는 경우
    dp[0] = sticker[0]
    dp[1] = sticker[0]
    for i in range(2, len(sticker) - 1): # 첫번째 떼서 마지막꺼는 못뗌
        dp[i] = max([dp[i - 1], dp[i - 2] + sticker[i]])

    # 첫번째 스티커 떼지 않는 경우
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max([dp2[i - 1], dp2[i - 2] + sticker[i]])

    return max([dp[len(sticker) - 2], dp2[len(sticker) - 1]])

"""
원형 문제를 선형 문제로 바꾸어 생각해 보자!
dp[i] : i까지 최대값
dp[i] = max([dp[i - 1], dp[i - 2] + sticker[i]])
    >> dp[i - 1] : 바로 전 스티커를 떼는 경우 (i번째 스티커는 못뗌)
    >> dp[i - 2] + sticker[i] : 2개 전 스티커를 떼는 경우 (i번째 스티커 떼어야 최대)

#* lv4. 도둑질 과 같은 문제!
"""