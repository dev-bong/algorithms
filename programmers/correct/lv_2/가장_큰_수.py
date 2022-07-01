def comp(a,b):
    """
    e.g. "97", "978" 이 전달되었을 때
    "97978", "97897" 중에 "97978"이 크므로 "97"이 앞에 와야 함
    """
    if int(a+b) > int(b+a):
        return True
    else:
        return False

def merge_sort(array): # 전달된 숫자들을 우선 순위에 맞게 정렬 (merge sort)
    if len(array) < 2:
        return array
    mid = len(array) // 2
    low_arr = merge_sort(array[:mid])
    high_arr = merge_sort(array[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if comp(low_arr[l], high_arr[h]):
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    
    return merged_arr

def solution(numbers):
    answer = ""
    sort_res = []
    numbers_dict = {i : [] for i in range(0,10)}

    # 맨 앞자리 기준으로 숫자들을 나눔
    for n in numbers:
        numbers_dict[int(str(n)[0])].append(str(n))

    for i in range(9, -1, -1):
        if numbers_dict[i]:
            sort_res += merge_sort(numbers_dict[i])

    for sr in sort_res:
        answer += sr
    return str(int(answer))