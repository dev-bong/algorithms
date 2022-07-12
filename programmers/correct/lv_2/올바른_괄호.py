def solution(s):
    stack = []

    for item in s:
        if item == "(":
            stack.append(item)
        elif item == ")":
            if stack:
                stack.pop()
            else:
                return False

    # 괄호 쌍이 맞으면 스택이 비어야 정상
    return False if stack else True