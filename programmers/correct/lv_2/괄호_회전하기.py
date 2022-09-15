def is_correct(s_list): # 올바른 괄호 문자열인지 검사
    stack = [] # stack 이용

    for item in s_list:
        if stack:
            top = stack[-1]
            if top == "[" and item == "]":
                stack.pop()
            elif top == "(" and item == ")":
                stack.pop()
            elif top == "{" and item == "}":
                stack.pop()
            else:
                stack.append(item)
        else:
            stack.append(item)
    
    return True if not stack else False # 끝나고 스택이 비어있으면 올바른 문자열

def rotate(s_list, n): # s_list를 n만큼 왼쪽으로 회전
    res = []

    for i in range(n, len(s_list) + n):
        res.append(s_list[i % len(s_list)])
    return res

def solution(s):
    answer = 0
    s_list = list(s)
    
    for i in range(len(s)):
        r = rotate(s_list, i)
        if is_correct(r):
            answer += 1
    return answer