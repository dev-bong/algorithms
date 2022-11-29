
#! 첫번째 풀이 : 시간 초과
def num_of_remain(num):
    #* 모든 수의 약수를 구하는 부분에서 시간이 오래 걸림
    res = 1
    for n in range(1, num):
        if num % n == 0:
            res += 1
    return res

def solution(number, limit, power):
    answer = 0

    for num in range(1, number + 1):
        w = num_of_remain(num)
        answer += power if w > limit else w
    return answer


#! 두번째 풀이 : 통과 (최고 시간 : 1860 ms)
def weapon(num, limit, power):
    #* 약수는 짝을 이루는 것을 이용
    res = 0
    center = int(num ** 0.5)
    for n in range(1, center + 1): #* root(num) 까지만 검사
        if num % n == 0:
            if n ** 2 == num: #* 제곱수일 경우에는 하나만 더하기
                res += 1
            else:
                res += 2
        if res > limit: #* 약수의 개수 > limit 일 경우 계산 그만
            return power
    return res

def solution(number, limit, power):
    answer = 0

    for num in range(1, number + 1):
        w = weapon(num, limit, power)
        answer += w
    return answer