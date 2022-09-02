from collections import deque

def del_dupl(string):
    if not string:
        return

    res = deque([string.popleft()])

    while string:
        cur = string.popleft() # 문자열 앞에부터 뽑음
        if not res: # res 비어있으면 넣고 땡
            res.append(cur)
            continue
        ex = res[-1]

        if cur == ex: # 전에 뽑은거랑 같으면 (중복)
            res.pop() # 전에 뽑은거랑, 지금 뽑은거랑 짝지어 날려버리기
        else:
            res.append(cur)
    return res

def solution(s):
    sl = list(s)
    sl = deque(s)

    r = del_dupl(sl)

    return 0 if r else 1