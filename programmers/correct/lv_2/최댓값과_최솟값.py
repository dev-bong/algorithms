def solution(s):
    nums = [int(n) for n in s.split(" ")] # 문자열에서 숫자 추출
    nums.sort()
    return " ".join([str(nums[0]), str(nums[-1])]) # 정렬한 것에서 최소, 최대