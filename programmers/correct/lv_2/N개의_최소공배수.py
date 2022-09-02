def solution(arr):
    arr.sort()
    max_val = arr[-1] # 제일 큰 수를 기준으로
    remain = arr[:-1]

    num = 1
    while True:
        cnt = 0
        for r in remain:
            if (max_val * num) % r == 0: # 제일 큰 수의 배수들 체크하며 남은 수들로 나누어 떨어지는지 체크
                cnt += 1

        if cnt == len(remain):
            return max_val * num
        num += 1