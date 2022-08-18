from itertools import permutations

def distance(a, b, size):
    # 두 인덱스 사이 거리 계산
    idxs = [a, b]
    idxs.sort()
    sml, big = idxs

    right = big - sml # 작은쪽에서 큰쪽으로 가는 거리 (오른쪽 방향)
    left = sml + size - big # 작은쪽에서 큰쪽으로 가는 거리 (왼쪽 방향)

    return min([left, right])

def solution(name):
    len_name = len(name)
    num_of_cmd = []
    not_A_idx = []
    min_lr_cmd = 50 # 대충 큰값으로.. (name 최대 길이가 20이라서)
    
    # 각 인덱스별 필요한 커맨드 수 (위아래 커맨드)
    for i in range(len_name):
        up_cmd = ord(name[i]) - ord("A")
        down_cmd = ord("Z") - ord(name[i]) + 1
        optimum_cmd = min([up_cmd, down_cmd]) # 위, 아래 커맨드 중 적게 필요한 쪽 선택
        num_of_cmd.append(optimum_cmd)
        if optimum_cmd != 0 and i != 0:
            not_A_idx.append(i) # 도착해서 위,아래 커맨드를 입력해야하는 인덱스 수집.. "A"인 곳은 방문 안해도 됨

    answer = sum(num_of_cmd) # 위아래 커맨드 수 모두 합치기

    # 왼,오른 커맨드 수 계산
    cases = permutations(not_A_idx, len(not_A_idx))
    for case in cases:
        if not case: # case가 없는 경우 그냥 리턴 (모두 "A"거나, 인덱스 0 빼고 모두 "A"인 경우?)
            return answer
        tmp_dis = distance(0, case[0], len_name)
        for i in range(len(not_A_idx) - 1):
            if tmp_dis > min_lr_cmd: # 더하다가 현재 최소값보다 커질 경우 계산 멈추기 (시간 단축을 위해)
                break
            tmp_dis += distance(case[i], case[i+1], len_name)

        min_lr_cmd = min([min_lr_cmd, tmp_dis])
    
    answer += min_lr_cmd

    return answer