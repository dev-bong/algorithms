import math
import itertools

def is_prime(num): # 소수 판별 : sqrt(num) 이하의 수 중에서 약수 찾기
    if num in [0, 1]:
        return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def num_combination(numbers): # 주어진 숫자 문자열 쪼개서 조합 구하기
    len_of_nums = len(numbers)
    nums_split = [numbers[i] for i in range(len_of_nums)] # 쪼개진 숫자들

    res = [int(ns) for ns in nums_split] # C(n,1)
    for i in range(2, len_of_nums+1): # C(n,2) ~ C(n,n)
        comb_cases = list(itertools.permutations(nums_split, i))
        for c_case in comb_cases:
            case = ""
            for cc in c_case:
                case += cc
            res.append(int(case))

    return res

def solution(numbers):
    answer = 0
    num_combs = num_combination(numbers)
    num_combs = list(set(num_combs))

    for nc in num_combs: # 숫자 조합 중에 소수 개수 세기
        if is_prime(nc):
            answer += 1

    return answer