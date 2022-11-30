def area_size(a1, a2):
    return (1/2) * (a1 + a2) # 사다리꼴 넓이

def collatz(num, graph, area):
    # collatz 그래프 구하면서 1칸당 넓이도 같이 구하기
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = (3 * num) + 1
        area.append(area_size(num, graph[-1]))
        graph.append(num)

def solution(k, ranges):
    answer = []
    graph = [k]
    area = []
    collatz(k, graph, area)
    c_len = len(area)

    for st, end in ranges:
        end = c_len + end
        if st == end:
            answer.append(float(0))
        elif st > end:
            answer.append(float(-1))
        else:
            answer.append(float(sum(area[st:end])))
    return answer