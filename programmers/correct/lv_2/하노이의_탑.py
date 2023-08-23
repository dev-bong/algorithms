def hanoi(frm, to, n):
    if n == 1:
        answer.append([frm, to])
    else:
        empty = 6 - frm - to # frm + to + empty = 6
        hanoi(frm, empty, n - 1)
        answer.append([frm, to])
        hanoi(empty, to, n - 1)

def solution(n):
    global answer
    answer = []
    hanoi(1, 3, n)
    return answer

"""
다시 이해해보고 설명써보기
"""