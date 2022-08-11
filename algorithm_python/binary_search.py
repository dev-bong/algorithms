# 이진 탐색 비재귀적 ver
def binary_search(arr, target):
    bot_idx, top_idx = (0, len(arr)-1)

    while bot_idx <= top_idx:
        mid_idx = (bot_idx + top_idx) // 2
        
        if arr[mid_idx] > target:
            top_idx = mid_idx - 1
        elif arr[mid_idx] < target:
            bot_idx = mid_idx + 1
        else:
            return mid_idx
    
    return -1 # 탐색 실패

# 이진 탐색 재귀 ver
def binary_search2(arr, bot_idx, top_idx, target):
    if bot_idx > top_idx: # 탐색 실패
        return -1

    mid_idx = (bot_idx + top_idx) // 2

    if arr[mid_idx] > target:
        return binary_search2(arr, bot_idx, mid_idx - 1, target)
    elif arr[mid_idx] < target:
        return binary_search2(arr, mid_idx + 1, top_idx, target)
    else:
        return mid_idx