def solution(n):
    sqrt_n = n ** 0.5
    sqrt_int = int(sqrt_n)

    if sqrt_n - sqrt_int == 0: # 루트씌운 수의 소수부가 있는지 없는지로 판단
        return int((sqrt_n + 1) ** 2)
    else:
        return -1