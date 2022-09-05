def finn(start, target):
    # start부터 임의의 n개 숫자의 합이 target과 같게 되는 경우가 있는지 체크
    for n in range(1, 10001): # n : start부터 순서대로 선택된 숫자들의 개수
        s = (n * (start + start + n - 1))/2 # start 부터 n 개 숫자의 합 (등차수열의 합 공식)
        if s == target: # 조건을 만족하는 등차수열이 있으면 True
            return True
        elif s > target:
            break
    return False

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if finn(i, n):
            answer += 1

    return answer