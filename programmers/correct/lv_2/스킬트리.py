def solution(skill, skill_trees):
    # skill : 스킬 찍는 순서, 유저들이 제안?하는 스킬트리들
    answer = 0

    for s_tree in skill_trees:
        in_tree = ""
        start_with = True
        for s in s_tree: # 
            if s in skill: # 스킬 순서에 있는 스킬들 순서대로 추출
                in_tree += s

        for i in range(len(in_tree)):
            if in_tree[i] != skill[i]: # 스킬 순서랑 시작부터 비교해서 같으면 스킬트리 인정
                start_with = False
                break
        
        if start_with:
            answer += 1

    return answer

"""
ex> 스킬 순서 C - B - D 라고 할 때
앞에서 부터 비교해서 같아야함
    - 스킬 트리 C - ... - B - ... 이런식이면 인정
    - 스킬 트리 B - ... - D - ... 이런식이면 안됨
        - 순서는 맞지만 스킬 B를 찍으려면 앞에 있는 C를 무조건 찍어야함
        -> 따라서 앞에서 부터 비교해야함
"""