def binary_search(arr, target):
    st, end = (0, len(arr) - 1)
    res = None

    while st <= end:
        mid = (st + end) // 2

        if arr[mid] > target: # arr[mid] == target이면 동점이라서 승점을 얻을 수 없다. 승점을 얻는 경우만 체크
            end = mid - 1
            res = mid
        else:
            st = mid + 1
    return res

def solution(A, B):
    answer = 0
    
    B.sort() # 이진탐색을 위해 정렬

    for a in A:
        win = binary_search(B, a) # B에서 a를 이길수 있는 것 중에 가장 작은 것 찾기

        if win != None: #! if win: 으로 했다가 win = 0인 경우도 걸러져 버림
            del B[win]
            answer += 1
        else:
            B = B[1:]

    return answer