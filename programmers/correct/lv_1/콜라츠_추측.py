def collatz(num):
    return num // 2 if num % 2 == 0 else 3 * num + 1

def solution(num):
    answer = 0
    if num == 1:
        return 0
    while True:
        answer += 1
        num = collatz(num)
        if num == 1:
            return answer
        if answer >= 500:
            return -1