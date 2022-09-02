def k_base(num, k):
    # k진법으로 변환 (16진수까지)
    res = ""
    over_10 = ["A", "B", "C", "D", "E", "F"]

    while num:
        q = num // k
        r = num % k

        if r < 10:
            res += str(r)
        else:
            res += over_10[r - 10]

        num = q

    if not res:
        return "0"

    return res[::-1]

def solution(n, t, m, p):
    # n : 진법, t : 구할 숫자 개수, m : 참가하는 인원 수, p : 인원 중 튜브의 순서
    total_answers = ""
    tube_answer = ""
    total_num = t * m # 구해야하는 총 숫자 개수
    cur_num = 0 # 현재 구한 숫자 개수
    num = 0

    for num in range(total_num):
        if cur_num > total_num:
            break
        tmp = k_base(num, n)
        total_answers += tmp
        cur_num = len(tmp)

    for i in range(p - 1, total_num, m):
        tube_answer += total_answers[i]

    return tube_answer