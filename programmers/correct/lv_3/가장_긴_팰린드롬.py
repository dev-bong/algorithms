def palindrome(s, center, is_even): # center를 중심으로 하는 최대 palindrome 길이
    st = 0
    end = len(s) - 1
    idx = 1

    if is_even:
        res = 2
        c1 = center[0]
        c2 = center[1]
    else:
        res = 1
        c1 = center
        c2 = center

    while (c1 - idx) >= st and (c2 + idx) <= end: # 중심에서 양방향으로 한칸씩 가면서 같은 문자인지 비교
        if s[c1 - idx] == s[c2 + idx]:
            res += 2
            idx += 1
        else:
            break
    return res

def solution(s):
    answer = []

    for i in range(len(s)): # i를 중심으로하는 최대 palindrome 구하기 (홀수 palindrome)
        answer.append(palindrome(s, i, False))

    for i in range(0, len(s) - 1): # i, i+1을 중심으로 하는 최대 palindrome 구하기 (짝수 palindrome)
        if s[i] == s[i + 1]:
            answer.append(palindrome(s, (i, i + 1), True)) # 짝수 palindrome 구할때는 center를 tuple로 전달

    return max(answer)