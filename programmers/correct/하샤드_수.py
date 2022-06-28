def solution(x):
    sx = str(x)
    xsum = sum([int(num) for num in sx]) # 문자열로 바꿔서 각 자리수 더하기

    return True if x % xsum == 0 else False