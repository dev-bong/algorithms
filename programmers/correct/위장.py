def solution(clothes):
    cloth_type_table = {}

    for cloth in clothes:
        if cloth[1] in cloth_type_table:
            cloth_type_table[cloth[1]] += 1
        else:
            cloth_type_table[cloth[1]] = 1
    
    #num_of_types = len(cloth_type_table.keys())
    type_values = list(cloth_type_table.values())

    answer = 1
    for tv in type_values:
        answer *= (tv + 1)
    answer -= 1
    """
    ex> 옷의 종류가 (headgear : 2, eyewear : 1, shoes : 2) 일 때

    1. 이전 시간 초과 풀이
        1) 옷 1 종류만 입을 경우 : 2 + 1 + 2
        2) 옷 2 종류 입을 경우 : 2*1 + 1*2 + 2*2
        3) 3 종류 다 입을 경우 : 2*1*2
        - 다 더하면 : 17
        - n 종류 입을 경우 계산을 위해 곱해질 숫자 조합을 선택하고 그걸 계산하느라 for문이 많이 쓰이게 됨

    2. 시간 초과 해결 풀이
        (2+1)*(1+1)*(2+1) - 1 = 17
        - 각 종류에 +1은 안입는 경우를 하나의 옷이라고 생각
        - -1은 모두 안입는 경우는 없으므로 빼주기
    """

    return answer
# TODO : hash로 풀어보기