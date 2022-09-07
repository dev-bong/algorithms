def get_w(lzw_list, msg):
    match = ""
    is_break = False
    for i in range(len(msg)):
        match += msg[i]
        if match not in lzw_list:
            is_break = True
            break
    if is_break: # msg의 처음부터 일정부분까지만 사전에 존재하는 경우
        lzw_list.append(match) # 사전에 존재하는 부분 + 다음 문자 >> 사전에 넣기
        return i
    else: # msg 전체가 사전에 존재
        return len(msg)

def solution(msg):
    answer = []
    lzw_list = [chr(ord("A") + i - 1) for i in range(27)] # index = 딕셔너리 인덱스, value = 값

    while msg:
        w_idx = get_w(lzw_list, msg)
        w = msg[:w_idx]
        msg = msg[w_idx:]
        answer.append(lzw_list.index(w))

    return answer