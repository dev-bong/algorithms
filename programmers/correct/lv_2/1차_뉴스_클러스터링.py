def is_alphabet(ch): # 해당 문자가 알파벳인지 검사. 아스키코드 이용
    ascii_ch = ord(ch)

    if (ord("a") <= ascii_ch and ord("z") >= ascii_ch) or (ord("A") <= ascii_ch and ord("Z") >= ascii_ch):
        return True
    else:
        return False

def zaccard(s1, s2):
    union = 0
    inter = 0
    s1_keys = set(s1.keys())
    s2_keys = set(s2.keys())

    # union
    union_keys = s1_keys | s2_keys
    for uk in union_keys:
        if uk in s1_keys and uk in s2_keys:
            union += max([s1[uk], s2[uk]])
        else:
            if uk in s1_keys:
                union += s1[uk]
            elif uk in s2_keys:
                union += s2[uk]
    
    # intersection
    inter_keys = s1_keys & s2_keys
    for ik in inter_keys:
        inter += min([s1[ik], s2[ik]])
    return inter / union

def solution(str1, str2):
    s1 = {}
    s2 = {}

    for i in range(len(str1) - 1):
        if not is_alphabet(str1[i]) or not is_alphabet(str1[i + 1]): # 2개씩 떼서 원소를 만드는데 알파벳 아닌게 들어가있으면 버리기
            continue

        two_wd = (str1[i] + str1[i + 1]).lower() # 원소 소문자로 만들어서 넣기
        if two_wd in s1:
            s1[two_wd] += 1
        else:
            s1[two_wd] = 1

    for i in range(len(str2) - 1):
        if not is_alphabet(str2[i]) or not is_alphabet(str2[i + 1]):
            continue

        two_wd = (str2[i] + str2[i + 1]).lower()
        if two_wd in s2:
            s2[two_wd] += 1
        else:
            s2[two_wd] = 1

    z = zaccard(s1, s2) if s1 or s2 else 1 # s1, s2 모두 비어있는 경우..
    return int(z * 65536)

"""
문제 정의에 따라 합집합, 교집합 구현
# TODO : 정규표현식 이용한 알파벳 판별? 만들어보기
    - isalpha??
"""