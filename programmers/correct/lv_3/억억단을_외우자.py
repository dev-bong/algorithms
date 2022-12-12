
#! 기존 풀이 (시간 초과 8, 9, 10)
def num_dan(num): # 해당 숫자가 억억단에서 몇번 나왔는지
    res = 0
    root_num = num ** 0.5
    for i in range(1, int(root_num) + 1):
        if num % i == 0:
            res += 1 if i == root_num else 2
    return res

def solution(e, starts):
    answer = []
    min_start = min(starts)
    num_appear = []

    for i in range(min_start, e + 1): #? part 1
        num_appear.append((i, num_dan(i)))

    for start in starts: #? part 2
        tmp = num_appear[start - min_start:]
        tmp.sort(key=lambda r: (-r[1], r[0]))

        answer.append(tmp[0][0])

    return answer

"""
#? part 1
    - 약수의 개수를 구하는데 시간이 오래걸림

#? part 2
    - num_appear 배열을 매번 슬라이싱 & 정렬 해야함..
"""


#! 풀이 2 - part 2 속도 up (시간초과 9, 10)
def num_dan(num): # 해당 숫자가 억억단에서 몇번 나왔는지
    res = 0
    root_num = num ** 0.5
    for i in range(1, int(root_num) + 1):
        if num % i == 0:
            res += 1 if i == root_num else 2
    return res

def solution(e, starts):
    answer = []
    min_start = min(starts)
    num_appear = []

    for i in range(min_start, e + 1):
        num_appear.append((i, num_dan(i)))
    
    num_appear.sort(key=lambda r: (-r[1], r[0])) #* 미리 정렬 (한번만 정렬)

    for start in starts:
        for na in num_appear: #* 정렬된 list에서 탐색
            if na[0] >= start and na[0] <= e:
                answer.append(na[0])
                break

    return answer


#! 풀이 3 - part 1 속도 up (시간초과 9, 10)
def solution(e, starts):
    answer = []
    num_appear = [[i, 0] for i in range(e + 1)]

    #* 약수 개수 구하는 알고리즘 변경
    for n in range(1, e + 1):
        tmp = n
        while tmp <= e:
            num_appear[tmp][1] += 1
            tmp += n
    
    num_appear.sort(key=lambda r: (-r[1], r[0]))

    for start in starts:
        for na in num_appear:
            if na[0] >= start and na[0] <= e:
                answer.append(na[0])
                break

    return answer