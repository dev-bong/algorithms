def solution(strings, n):
    strings.sort() # 사전순으로 먼저 정렬 (문자열 요소 리스트의 정렬은 사전순으로 정렬된다)
    strings.sort(key=lambda r:r[n])
    return strings