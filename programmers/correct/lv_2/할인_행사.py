def solution(want, number, discount):
    answer = 0
    for i in range(0, len(discount) - 9):
        day10 = discount[i:i + 10]
        match = 0
        for j in range(len(want)):
            if day10.count(want[j]) == number[j]:
                match += 1
        if match == len(want):
            answer += 1
    return answer

#? 이게 왜 lv2 ??