def solution(n):
    answer = []
    str_li_n = list(str(n))
    for i in range(len(str_li_n)-1, -1, -1):
        answer.append(int(str_li_n[i]))
    return answer

# 문자열 뒤집기 다른 방법??