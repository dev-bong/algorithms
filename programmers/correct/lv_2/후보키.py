from itertools import combinations

def is_key(relation, key): # key를 relation에서 진짜 key로 사용할 수 있는지 체크 (유일성 체크)
    s = set()

    for r in relation:
        key_attrs = tuple([r[k] for k in key]) # key에 속한 attr들을 아이템에서 뽑아 튜플로 만들어 집합에 넣기
        s.add(key_attrs)

    return True if len(relation) == len(s) else False # 진짜 key일 경우 attr 튜플들이 유니크할 것이므로 len(relation) == len(s)를 만족하게 됨

def solution(relation):
    correct_keys = []
    attrs = [i for i in range(len(relation[0]))] # attr의 개수에 따라 왼쪽부터 0번부터 붙여서 나열
    
    for key_size in range(1, len(relation[0]) + 1): # key_size를 증가시키면서 체크
        can_keys = combinations(attrs, key_size) # 해당 key_size일 때 attr들의 조합 경우들
        
        for c_key in can_keys:
            is_subset = False
            # c_key의 부분집합이 이미 correct_keys에 존재하는 경우 (최소성)
            for cor_key in correct_keys:
                if len(set(cor_key) - set(c_key)) == 0:
                    is_subset = True
                    break
            if is_subset:
                continue
            if is_key(relation, c_key): # 최소성은 만족하는 경우 유일성 체크
                correct_keys.append(c_key)

    return len(correct_keys)

# TODO : 4개의 컬럼을 조합하는 경우의 수 4비트로 표현해 보기? 1100, 0101 등..
# - 이 경우 subset 여부는 비트연산을 통해서..