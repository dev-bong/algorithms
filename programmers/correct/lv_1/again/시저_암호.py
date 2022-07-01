def caesar(char, num):
    ascii_char = ord(char)

    if ascii_char >= ord("a") and ascii_char <= ord("z"): # 소문자 범위
        ascii_res = ascii_char + num
        if ascii_res > ord("z"):
            ascii_res = ord("a") + ascii_res - ord("z") - 1
        return chr(ascii_res)
    elif ascii_char >= ord("A") and ascii_char <= ord("Z"): # 대문자 범위
        ascii_res = ascii_char + num
        if ascii_res > ord("Z"):
            ascii_res = ord("A") + ascii_res - ord("Z") - 1
        return chr(ascii_res)
    else:
        return char

def solution(s, n):
    answer = ""

    for ch in s:
        answer += caesar(ch, n)
    return answer