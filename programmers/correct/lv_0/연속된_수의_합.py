def solution(num, total):
    st = (((2 * total) / num) - num + 1) / 2
    return [n for n in range(int(st), int(st) + num)]

"""
문제를 수식으로 나타내면

total = (num * (a + b)) // 2 #? 등비수열 공식
위 식을 만족하는 a, b를 찾고 a ~ b 사이의 수로 이루어진 수열을 리턴하는 것

    a부터 시작하는 num개 숫자의 합이므로, b = a + num - 1 이 성립
    >> total = (num * (2 * a + num - 1)) // 2
    ... 변환을 거쳐
    >> 2 * a = ((2 * total) / num) - num + 1
"""