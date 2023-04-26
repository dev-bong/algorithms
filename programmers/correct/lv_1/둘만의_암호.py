def solution(s, skip, index):
    answer = ''
    skip_asc = []
    
    for sk in skip:
        skip_asc.append(ord(sk) - ord("a"))

    for a in s:
        idx = ord(a) - ord("a")

        for i in range(index):
            idx = (idx + 1) % 26

            while idx in skip_asc:
                idx = (idx + 1) % 26

        answer += chr(idx + ord("a"))
    return answer