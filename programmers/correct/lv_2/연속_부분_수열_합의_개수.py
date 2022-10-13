def solution(elements):
    sub_sums = set(elements) # 부분수열 길이가 1인 경우의 합으로 초기화
    size = len(elements)
    elements = elements * 2

    for sub_len in range(2, size + 1): # 부분수열 길이 별로 합들 구하기
        for i in range(size):
            sub_sums.add(sum(elements[i : i + sub_len]))

    return len(sub_sums)

#! 실행시간이 좀 길긴함.. 개선 가능할듯??