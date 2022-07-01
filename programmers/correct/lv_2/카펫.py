def two_num_factorize(num): # num을 두 수의 곱으로 분해
    res = []
    for i in range(1, int(num ** 0.5) + 1): # sqrt(num) 까지의 약수만 체크
        if num % i == 0:
            res.append([i, num // i])
    return res

def solution(brown, yellow):
    """
    갈색 카펫들이 노란 카펫들을 감싸 직사각형을 만듦
    > 노란카펫들 = 가로 X 세로
    > 노란카펫들 + 갈색카펫들 = (가로 + 2) X (세로 + 2)
    """
    answer = []
    center = two_num_factorize(yellow)
    side = two_num_factorize(yellow + brown)

    for c in center:
        for s in side:
            if (c[0] + 2) == s[0] and (c[1] + 2) == s[1]: # 조건 체크
                return [s[1], s[0]]