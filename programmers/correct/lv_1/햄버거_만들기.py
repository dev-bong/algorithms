def solution(ingredient):
    answer = 0
    stack = []

    for ing in ingredient:
        if len(stack) >= 3 and ing == 1: # 쌓인 재료가 3개 이상이면서 현재 재료가 빵인 경우
            before = str(stack[-3]) + str(stack[-2]) + str(stack[-1])
            if before == "123": # 햄버거 만들 조건이 된다면
                for i in range(3):
                    stack.pop()
                answer += 1
            else:
                stack.append(ing)
        else:
            stack.append(ing)

    return answer