def find(num):
    if num % 2 == 0: # num이 짝수
        return num + 1
    else: # num이 홀수
        bin_num = list("0" + bin(num)[2:]) # 맨앞에 0 하나 더 추가
        for i in range(len(bin_num) - 1, -1, -1):
            if bin_num[i] == "0":
                bin_num[i] = "1"
                bin_num[i + 1] = "0"
                break
        return int("".join(bin_num), 2)

def solution(numbers):
    answer = []

    for num in numbers:
        answer.append(find(num))

    return answer

"""
홀수일 경우 규칙성을 찾아냄
1 :  01 >> 10 (2)
3 :  011 >> 101 (5)
5 :  101 >> 110 (6)
7 :  111 >> 1011 (11)
9 :  1001 >> 1010 (10)
11 :  1011 >> 1101 (13)
13 :  1101 >> 1110 (14)
15 :  01111 >> 10111 (23)
17 :  10001 >> 10010 (18)
19 :  10011 >> 10101 (21)

    끝에서부터 앞으로 가면서 0이 등장하는 순간, 뒤의 1이랑 위치를 바꿔줌
"""


#! 아래는 시간 초과 풀이
def find(num):
    if num % 2 == 0: # num이 짝수. 짝수일 때는 끝자리가 항상 0이므로 1을 더하는 것이 만족하는 최소값임
        return num + 1
    else: # num이 홀수
        nxt = num + 1
        while True: # 1씩 더해가면서 조건을 만족하는 값 찾기 #! 이부분에서 시간이 많이 소요됨
            xor = bin(num ^ nxt)
            if xor.count("1") <= 2:
                return nxt
            nxt += 1

def solution(numbers):
    answer = []

    for num in numbers:
        answer.append(find(num))

    return answer