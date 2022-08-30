"""
1. n진수 >> 10진수
    #? str -> int
    int(string, base) 형태로 활용. base 진법의 string을 10진법 정수로 바꾸어줌
    아래 테스트 케이스에서 이용 

2. 10진수 >> 2진수, 8진수, 16진수
    #? int -> str
    bin(10), oct(10), hex(10)
    각각 앞에 "0b", "0o", "0x" 가 붙음

3. 10진수 >> n진수
    #? int -> str
    아래 함수 이용

    * n진법 변환
        그 수를 0이 될 때까지 n으로 나누고, 그 나머지를 거꾸로 읽어 올라가면 된다

4. n진수 >> k진수
    10진수로 변경 뒤, k진수로 변경

# TODO : divmod 이용? import string 이용?
"""

def n_base(num, n):
    # num을 k진법으로 변환 (16진수까지)
    res = ""
    over_10 = ["A", "B", "C", "D", "E", "F"] # k가 11 이상일 때 사용

    while num:
        q = num // n
        r = num % n

        if r < 10:
            res += str(r)
        else:
            res += over_10[r - 10]

        num = q

    if not res:
        return "0" # 0이 입력된 경우

    return res[::-1]

# 테스트 케이스
print(n_base(6, 2), int(n_base(6, 2), 2))
print(n_base(38, 3), int(n_base(38, 3), 3))
print(n_base(4000, 16), int(n_base(4000, 16), 16))

print(bin(10), oct(10), hex(10))