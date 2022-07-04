def bin_list(length, num):
    bin_num = bin(num)[2:]
    len_bin = len(bin_num)

    if length > len_bin:
        bin_num = "0" * (length - len_bin) + bin_num
    return [int(bn) for bn in list(bin_num)]

def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    
    for i in range(n):
        map1.append(bin_list(n, arr1[i]))
        map2.append(bin_list(n, arr2[i]))

    for i in range(n):
        tmp = ""
        for j in range(n):
            if map1[i][j] or map2[i][j]:
                tmp += "#"
            else:
                tmp += " "
        answer.append(tmp)
    return answer