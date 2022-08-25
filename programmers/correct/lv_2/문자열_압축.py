def compress(k, s):
    # k : 압축 단위, s : 문자열
    ex_cut = None
    mid_stage = [] # (단위 문자열 개수, 단위 문자열) 로 이루어진 리스트
    res = "" # 압축 결과
    for i in range(k, len(s) + k, k):
        cut = s[i - k:i] #? 슬라이싱할 때 오른쪽 인덱스가 리스트 범위 넘으면???.. 일단 되는거 같긴 함
        if ex_cut == cut:
            mid_stage[-1][0] += 1
        else:
            mid_stage.append([1, cut])
        ex_cut = cut
    
    for m in mid_stage:
        if m[0] == 1:
            res += m[1]
        else:
            res += (str(m[0]) + m[1])
    
    return len(res) # 압축 결과 길이

def solution(s):
    str_len = len(s)
    comp_len_list = []

    for i in range(1, str_len + 1): # 압축 단위 1 ~ str_len 까지 하면서 저장
        comp_len_list.append(compress(i, s))

    return min(comp_len_list) # 압축 길이 중 최소값

# 테스트 케이스
print(solution("aabbaccc"), 7)
print(solution("ababcdcdababcdcd"), 9)
print(solution("abcabcdede"), 8)
print(solution("abcabcabcabcdededededede"), 14)
print(solution("xababcdcdababcdcd"), 17)