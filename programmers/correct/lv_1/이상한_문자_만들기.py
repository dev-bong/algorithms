def word_trans(word): # 특정 단어를 번갈아가면서 대소문자로 설정
    big_flag = True
    res = ""
    for ch in word:
        if ch == " ":
            res += ch
        elif big_flag:
            big_flag = not big_flag
            res += ch.upper()
        else:
            big_flag = not big_flag
            res += ch.lower()

    return res


def solution(s):
    answer = ""
    words = list(s.split(" "))

    for wd in words:
        answer += word_trans(wd)
        answer += " "

    return answer[:-1] # 마지막에 들어간 공백 제거