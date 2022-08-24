def cal(arr_str):
    # arr_str : 숫자와 연산자 나열
    # 입력된 나열에서 연산 최대값
    size = len(arr_str)

    if arr_str in memo: # memo에 있으면 메모된 값 리턴
        return memo[arr_str]
    elif "+" not in arr_str and "-" not in arr_str: # +, - 가 존재하지 않는 문자열 : 양수
        memo[arr_str] = [int(arr_str), int(arr_str)]
        return memo[arr_str]
    elif arr_str[0] == "-" and "-" not in arr_str[1:] and "+" not in arr_str[1:]: # 맨 앞이 -이고 그 뒤로 연산자 없는 문자열 : 음수
        memo[arr_str] = [int(arr_str), int(arr_str)]
        return memo[arr_str]
    else:
        candidate = []
        for i in range(size):
            if arr_str[i] not in ["+", "-"]:
                continue
            # 연산자를 만날경우 왼쪽 파트, 오른쪽 파트로 나누기
            op = arr_str[i]
            left = arr_str[:i]
            right = arr_str[i+1:]
            if not left or not right:
                continue

            left_cal = cal(left)
            right_cal = cal(right)
            for l in left_cal:
                for r in right_cal:
                    if op == "-":
                        candidate.append(l - r)
                    elif op == "+":
                        candidate.append(l + r)
        memo[arr_str] = [max(candidate), min(candidate)]
        return memo[arr_str]

def solution(arr):
    arr_str = ""
    global memo
    memo = {}

    for a in arr: # 숫자와 연산자 나열을 문자열로 만들기 (리스트로 할 경우 call by value처럼 되어서 다루기 어려움)
        arr_str += a

    answer = cal(arr_str)

    return answer[0]


"""
#! 덧셈의 최대값 : 최대 + 최대, ***뺄셈의 최대값 : 최대 - 최소

#! 아래처럼 문자열로 안바꾸고 해봤는데 시간이 좀더 걸려서 효율성 케이스 3번을 통과 못함 (시간 초과)
def cal(arr):
    size = len(arr)
    key = str(arr)

    if key in memo:
        return memo[key]
    elif size == 1:
        memo[key] = [int(arr[0]), int(arr[0])]
        return memo[key]
    else:
        candidate = []
        for i in range(1, size, 2):
            op = arr[i]
            left = cal(arr[:i])
            right = cal(arr[i+1:])

            for l in left:
                for r in right:
                    if op == "-":
                        candidate.append(l - r)
                    elif op == "+":
                        candidate.append(l + r)
        memo[key] = [max(candidate), min(candidate)]
        return memo[key]

def solution(arr):
    global memo
    memo = {}

    answer = cal(arr)

    return answer[0]
"""