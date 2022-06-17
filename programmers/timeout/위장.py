from itertools import combinations

def solution(clothes):
    answer = 0
    cloth_type_table = {}

    for cloth in clothes:
        if cloth[1] in cloth_type_table:
            cloth_type_table[cloth[1]] += 1
        else:
            cloth_type_table[cloth[1]] = 1
    
    num_of_types = len(cloth_type_table.keys())
    type_values = list(cloth_type_table.values())

    for n in range(1, num_of_types+1):
        comb = list(combinations(type_values, n))
        
        for c in comb:
            tmp = 1
            for i in c:
                tmp *= i
            answer += tmp

    return answer