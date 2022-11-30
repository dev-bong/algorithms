def solution(k, tangerine):
    answer = 0
    tang_dict = dict()
    tang_num = []

    # 귤 크기 : 귤 개수 형태 딕셔너리 만들기
    for t in tangerine:
        if t in tang_dict:
            tang_dict[t] += 1
        else:
            tang_dict[t] = 1
    
    # (귤 크기, 귤 개수) 원소로 하는 리스트 만들기
    for td in tang_dict:
        tang_num.append((td, tang_dict[td]))
    
    # 귤 개수 순으로 정렬
    tang_num.sort(key = lambda r: r[1])
    
    # 귤 개수 큰 귤 종류부터 박스에 포장
    while k > 0:
        _, tn = tang_num.pop()
        k -= tn
        answer += 1
    return answer