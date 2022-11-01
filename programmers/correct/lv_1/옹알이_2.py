def solution(babbling):
    answer = 0
    babs = ["aya", "ye", "woo", "ma"] # 옹알이 요소

    for bab in babbling:
        tmp = bab
        ex = None
        possible = True
        while tmp:
            cur = None
            for b in babs:
                if tmp.startswith(b):
                    cur = b
                    break

            if not cur or cur == ex: # 발음할 수 있는 단어가 없거나, 요소를 중복으로 말하는 경우 >> 발음 불가능함
                possible = False
                break

            tmp = tmp[len(cur):]
            ex = cur
        if possible:
            answer += 1

    return answer