from itertools import combinations

def solution(orders, course):
    answer = []
    order_set = [set(list(od)) for od in orders] # 각 order를 집합 형태로 변경
    intersections = set()
    intrsc_dict = {i : [0, []] for i in range(2, len(orders) + 1)} # 코스요리 메뉴 수 : [해당 코스요리 조합을 주문한 손님 수, 코스요리]

    for i in range(len(order_set)):
        for j in range(i + 1, len(order_set)): # 서로 다른 2개의 order를 뽑아서 교집합 추출
            intrsc = list(order_set[i] & order_set[j])
            if len(intrsc) == 2:
                intrsc.sort()
                intersections.add("".join(intrsc))
            if len(intrsc) > 2: # 교집합 메뉴 수가 2개 이상이면, 교집합 메뉴들로 만들 수 있는 조합들 추출..
                for k in range(2, len(intrsc)): # ex> 4개면 2개조합, 3개조합 계산
                    cases = combinations(intrsc, k)
                    for case in cases:
                        intersections.add("".join(sorted(list(case)))) # 계산한 조합들 넣기
                intrsc.sort()
                intersections.add("".join(intrsc))
    
    for intrsc in intersections:
        cur_max, _ = intrsc_dict[len(intrsc)]
        cnt = 0
        
        intrsc_set = set(intrsc)
        for od in order_set: # 해당 세트메뉴가 들어있는 주문들의 수 카운팅 (주문한 손님의 수)
            if intrsc_set & od == intrsc_set:
                cnt += 1

        if cnt > cur_max: # 이전에 가장 많이 주문한 세트메뉴보다 주문 수가 많으면 반영
            intrsc_dict[len(intrsc)][0] = cnt
            intrsc_dict[len(intrsc)][1] = [intrsc]
        elif cnt == cur_max: # 같으면 추가하기
            intrsc_dict[len(intrsc)][1].append(intrsc)
    
    for c in course:
        if c in intrsc_dict:
            answer.extend(intrsc_dict[c][1])

    return sorted(answer)