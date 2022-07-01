def solution(arr):
    min_idx = arr.index(min(arr))
    del arr[min_idx]
    
    if not arr:
        return [-1]
    return arr

# 입력받은 배열의 요소 위치를 보존해야 하기 때문에 정렬은 쓰면 안됨