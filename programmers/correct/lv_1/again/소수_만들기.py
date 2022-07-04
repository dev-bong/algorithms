from itertools import combinations

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    cases = combinations(nums, 3)
    sum_nums = [sum(case) for case in cases]
    """
    set으로 중복 제거했다가 틀림. 서로 다른 3가지 수를 골라 더해서 소수가 되는 경우의 수를 구하는 것이기 때문에
    합은 중복되도 괜찮음
    """

    for sn in sum_nums:
        if is_prime(sn):
            answer += 1
    return answer