def solution(number, k):
    stack = []

    for num in number:
        while stack and k > 0:
            # stack의 top(현재 숫자의 앞자리)이 현재 숫자보다 작으면 pop으로 제거
            # k번까지 계속해서 제거 ex> stack = [2,1], num = 9 면 1, 2 둘다 pop 해야함
            if stack[-1] < num:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(num)

    if k != 0: # k가 다 소모되지 않았을 경우 (끝가지 검색했는데 앞자리가 작은 경우의 수가 k보다 작은 경우)
        stack = stack[:-k] # 끝에서 빼기
    
    return "".join(stack)

"""
시간초과 해결을 위해 stack 이용한 알고리즘으로 변경!
"""