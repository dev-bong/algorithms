def solution(s):
    answer = []
    s = s.replace("}", "")
    s_split = s[1:].split("{")[1:]
    s_list = []
    
    for ss in s_split:
        tmp = set()
        for _ in ss.split(","):
            if _:
                tmp.add(int(_))
        s_list.append(tmp)

    s_list.sort(key = lambda r : len(r))
    
    answer.append(list(s_list[0])[0])
    for i in range(len(s_list) - 1):
        answer.append(list(s_list[i + 1] - s_list[i])[0])
        
    return answer