def solution(gems):
    answer = {
        "section" : None,
        "length" : len(gems) + 1
    }
    gem_types = set(gems)
    
    st, end = 0, 0
    cur_gems = {} #* set으로 변환하지 않기 위해 딕셔너리 형태 사용. 현재 st ~ end 범위에서 각 보석이 몇개씩 있는지
    cur_gems[gems[end]] = 1

    while st < len(gems):
        if len(gem_types) != len(cur_gems): # st ~ end 범위에서 없는 보석이 있는 경우
            end += 1
            if end >= len(gems):
                break
            if gems[end] in cur_gems:
                cur_gems[gems[end]] += 1
            else:
                cur_gems[gems[end]] = 1
        else: # st ~ end 범위에 모든 보석 존재
            if answer["length"] <= (end - st):
                pass
            else:
                answer["section"] = [st + 1, end + 1]
                answer["length"] = (end - st)
            cur_gems[gems[st]] -= 1
            if cur_gems[gems[st]] == 0:
                del cur_gems[gems[st]]
            st += 1
            if st >= len(gems):
                break 

    return answer["section"]

"""
#! https://school.programmers.co.kr/questions/14715
    >> sangbin lee 답변 참조
"""