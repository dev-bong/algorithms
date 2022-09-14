def is_correct(string): # "올바른 괄호 문자열"인지 검사
    stack = []

    for i in range(len(string)):
        cur = string[i]
        if stack:
            if stack[-1] == "(" and cur == ")":
                stack.pop()
                continue
        stack.append(cur)
    
    return False if stack else True

def split_balanced(string): # 앞에서부터 "균형잡힌 괄호 문자열"이 되는 지점을 알려주는 함수
    nl = 0
    nr = 0

    for s in string:
        if s == "(":
            nl += 1
        elif s == ")":
            nr += 1
        
        if nl == nr:
            return nl + nr
    return -1

def fix(string): # 문제 나온대로 짠 재귀함수
    if not string:
        return ""

    spl_idx = split_balanced(string) # 나누기
    u = string[:spl_idx]
    v = string[spl_idx:]

    if is_correct(u):
        return u + fix(v)
    else:
        tmp = ""
        for t in u[1:-1]:
            if t == "(":
                tmp += ")"
            elif t == ")":
                tmp += "("
        return "(" + fix(v) + ")" + tmp

def solution(p):
    return fix(p)