def solution(citations):
    answer = 0
    citations.sort()
    h_indices = []
    max_c = citations[-1]
    min_c = citations[0]
    citation_dict = {}
    uppers = []

    for c in citations: # 인용 수가 같은 논문끼리 모으기
        if c in citation_dict:
            citation_dict[c] += 1
        else:
            citation_dict[c] = 1
    """
    citation_dict = {
        인용 수 : 해당 인용 수의 논문들,
        ...
    }
    """

    for i in range(max_c, -1, -1): # 역순으로 가며 인용수 별로 해당 인용수 이상의 인용수를 가진 논문 개수 계산
        if i in citation_dict:
            if uppers:
                uppers.append((i, uppers[-1][1] + citation_dict[i]))
            else:
                uppers.append((i, citation_dict[i]))
        else:
            uppers.append((i, uppers[-1][1]))

    for u in uppers: # H index의 정의를 만족시키는 H 모으기
        if u[0] <= u[1]: # u[0] : 인용수, u[1] : 해당 인용수 이상의 인용수를 가진 논문의 수
            h_indices.append(u[0])
    answer = max(h_indices) # H index 후보 중 최대값
    return answer