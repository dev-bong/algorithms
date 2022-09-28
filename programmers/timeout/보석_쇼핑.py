
#! 그래도 좀 개선된 풀이. 효율성 테스트 12, 13, 15 실패
def solution(gems):
    answer = {
        "section" : None,
        "length" : len(gems) + 1
    }
    gem_types = set(gems)
    
    st, end = 0, 0
    cur_gems = {gt : 0 for gt in gem_types} #* set으로 변환하지 않기 위해 딕셔너리 형태 사용. 현재 st ~ end 범위에서 각 보석이 몇개씩 있는지
    cur_gems[gems[end]] += 1

    while st < len(gems):
        if 0 in cur_gems.values(): # st ~ end 범위에서 없는 보석이 있는 경우
            end += 1
            if end >= len(gems):
                break
            cur_gems[gems[end]] += 1
        else: # st ~ end 범위에 모든 보석 존재
            if answer["length"] <= (end - st):
                pass
            else:
                answer["section"] = [st + 1, end + 1]
                answer["length"] = (end - st)
            cur_gems[gems[st]] -= 1
            st += 1
            if st >= len(gems):
                break 

    return answer["section"]

"""
투포인터 알고리즘? 슬라이딩 윈도우??

투포인터 보고 영감을 받아서 짜봄.. (st, end 두개 움직이면서)
"""

#! 이전 풀이. 효율성 테스트 6번 빼고 다 시간초과
def solution(gems):
    answer = {
        "section" : None,
        "length" : len(gems) + 1
    }
    gem_types = set(gems)
    
    st, end = 0, 0
    cur_gems = [gems[end]]

    while st < len(gems):
        if gem_types - set(cur_gems): #! set으로 변환하는 부분이 O(N)이라고 함 (확인 필요)
            end += 1
            if end >= len(gems):
                break
            cur_gems.append(gems[end])
        else:
            if answer["length"] <= (end - st):
                pass
            else:
                answer["section"] = [st + 1, end + 1]
                answer["length"] = (end - st)
            cur_gems = cur_gems[1:] #! 슬라이싱도 시간 오래걸림 (deque 이용?)
            st += 1
            if st >= len(gems):
                break 

    return answer["section"]