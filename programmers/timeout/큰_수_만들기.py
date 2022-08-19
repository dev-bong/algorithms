def solution(number, k):
    num_list = [int(n) for n in number]
    ch = False

    while k > 0:
        # 앞에부터 두 수 씩 크기 비교
        for i in range(len(num_list) - 1):
            if num_list[i] < num_list[i+1]: # 앞의 수가 더 작으면 앞의 수 삭제
                ch = True
                break
        
        if ch:
            ch = False
            num_list.pop(i)
        else: # 끝까지 봤지만 앞의 수가 작은 경우가 없는 경우
            num_list.pop()

        k -= 1

    return "".join([str(n) for n in num_list])

"""
1. 앞에서 2개씩 검사
2. 2개중 앞에꺼가 더 작으면 앞에꺼 삭제
3. 끝까지 가면 마지막거 삭제

케이스 10번에서 시간초과
"""