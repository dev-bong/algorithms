def solution(prices):
    length = len(prices)
    answer = []

    for i in range(length):
        cnt = 0
        for j in range(i ,length):
            if prices[i] > prices[j] or j == length-1:
                break
            cnt += 1
        answer.append(cnt)

    return answer

#? 이전에는 왜 그렇게 복잡하게 풀려고 했을까..