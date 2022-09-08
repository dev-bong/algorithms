def solution(s):
    try_num = 0 # 이진변환 시도 횟수
    del_0 = 0 # 과정에서 제거된 0의 수

    ### 이진변환 ###
    while True:
        try_num += 1

        # 0 제거
        ex_len = len(s)
        s = s.replace("0", "")
        del0_len = len(s)
        del_0 += ex_len - del0_len

        # 0 제거 후 문자열 길이를 2진법으로 표현
        s = str(bin(del0_len))[2:]

        if s == "1":
            break

    return [try_num, del_0]