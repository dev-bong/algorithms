def round_parse(dart_res): # 다트 결과 한 라운드씩 파싱
    bonus_num = {
        "S" : 1,
        "D" : 2,
        "T" : 3
    }
    
    for i in range(len(dart_res)):
        if dart_res[i] in bonus_num:
            bonus = bonus_num[dart_res[i]]
            break
    score = int(dart_res[:i])
    opt = None
    remain = dart_res[i+1:]
    if remain and remain[0] in ["*", "#"]:
        opt = remain[0]
        remain = remain[1:]
    
    return (score ** bonus, opt, remain)

def solution(dartResult):
    answer = 0
    rounds = []

    while dartResult:
        s, o, remain = round_parse(dartResult)
        rounds.append([s, o])
        dartResult = remain
    
    for i in range(len(rounds)):
        score, opt = rounds[i]

        if opt == "*": # 주의! 스타상일 경우 바로 전 점수와 해당 회차 점수 2배
            if i == 0:
                rounds[i][0] = score * 2
            else:
                rounds[i][0] = score * 2
                rounds[i-1][0] = rounds[i-1][0] * 2
        elif opt == "#":
            rounds[i][0] = -score
        else:
            pass
    
    for round in rounds:
        answer += round[0]

    return answer