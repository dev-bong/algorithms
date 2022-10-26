
##### ! 처음 시간 초과 풀이 #####
def solution(topping):
    answer = 0
    #lside = []
    rside = deque(list())

    #? 오른쪽에서 부터 잘라보며 오른쪽 조각에는 토핑이 몇가지 있는지 세기
    tmp = set()
    for i in range(len(topping) - 1, 0, -1):
        tmp.add(topping[i])
        rside.appendleft(len(tmp))

    #? 왼쪽부터 잘라보며 왼쪽 조각에는 토핑 몇가지 있는지 세기
    tmp = set()
    for i in range(len(topping) - 1):
        tmp.add(topping[i])
        if len(tmp) == rside[i]:
            answer += 1
        #lside.append(len(tmp))
    #! 왼쪽, 오른쪽을 따로 세서 시간이 많이 걸린 것 같음
    # for i in range(len(lside)):
    #     if lside[i] == rside[i]:
    #         answer += 1

    return answer


##### * 시간 초과 통과 풀이 #####
def solution(topping):
    diff = [0] * (len(topping) - 1)

    lidx = 0
    ridx = len(topping) - 1
    lset = set()
    rset = set()
    while lidx < (len(topping) - 1): #? 반복문 한번에 왼쪽, 오른쪽 둘다 세기
        lset.add(topping[lidx])
        rset.add(topping[ridx])
        diff[lidx] += len(lset) # 왼쪽 조각 토핑 수는 더하고
        diff[ridx - 1] -= len(rset) # 오른쪽 조각 토핑 수는 빼기
        lidx += 1
        ridx -= 1

    return diff.count(0) # 토핑 수 차이가 0인 경우 세기


from collections import deque

