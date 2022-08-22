def solution(survey, choices):
    answer = ""
    types = ["R", "T", "C", "F", "J", "M", "A", "N"] # 성격유형 8개
    scores = {t : 0 for t in types} # 성격유형 별 점수
    q_num = len(survey)

    for i in range(q_num): # 성격유형 별 점수 계산
        lt = survey[i][0]
        rt = survey[i][1]

        if choices[i] < 4:
            score = 4 - choices[i]
            scores[lt] += score
        elif choices[i] > 4:
            score = choices[i] - 4
            scores[rt] += score
    
    print(scores)

    for i in range(0, 8, 2): # 대응되는 2가지 유형 중 점수가 높은 유형 선택
        lt = types[i]
        rt = types[i+1]
        if scores[lt] > scores[rt]:
            answer += lt
        elif scores[lt] < scores[rt]:
            answer += rt
        else:
            answer += min([lt, rt])
    return answer