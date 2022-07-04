def solution(n, lost, reserve):
    real_reserve = list(set(reserve) - set(lost)) # 집합을 이용해서 lost, reserve 공통부분 제거하기
    real_lost = list(set(lost) - set(reserve))
    no_cloth = []
    
    for l in real_lost:
        if (l - 1) in real_reserve:
            real_reserve.remove(l - 1)
        elif (l + 1) in real_reserve:
            real_reserve.remove(l + 1)
        else:
            no_cloth.append(l)
    return n - len(no_cloth)