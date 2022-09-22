from itertools import combinations

def solution(n, info):
    scores = [i for i in range(11)]
    apeech_scores = set([10 - i for i in range(len(info)) if info[i] > 0]) # 라이언이 쏘기 전 어피치가 딴 점수
    ryan_win_cases = {}

    for hit in range(1, n + 1): # hit = 1 : 한 곳에 다쏘기 ~~ hit = n  서로 다른 곳에 쏘기
        cases = combinations(scores, hit)
        for case in cases:
            need_arrows = sum([info[10 - c] + 1 for c in case]) # 해당 케이스의 점수를 따기위해 필요한 화살 수
            if need_arrows <= n: # 가능한 케이스인 경우
                ryan_score = sum(case)
                cur_apeech_score = sum(apeech_scores - set(case))
                if ryan_score >  cur_apeech_score:
                    # 라이언의 점수가 최대가 아니라 (라이언 점수 - 어피치 점수)가 최대
                    if ryan_score not in ryan_win_cases:
                        ryan_win_cases[ryan_score - cur_apeech_score] = [case]
                    else:
                        ryan_win_cases[ryan_score - cur_apeech_score].append(case)
    
    if ryan_win_cases: # 라이언이 이길 방법이 있는 경우
        max_ryan_score = max(ryan_win_cases.keys()) # 라이언이 낼 수 있는 최대 점수 차
        max_win_cases = ryan_win_cases[max_ryan_score]
        max_win_cases.sort(key = lambda r : r[0])

        win_case_targets = [] # 최대 점수 차 승리 경우들의 과녁판 상태?
        for mwc in max_win_cases:
            tmp = [0] * 11
            arrow_num = 0
            for a in mwc:
                tmp[10 - a] = info[10 - a] + 1
                arrow_num += info[10 - a] + 1
            
            if arrow_num != n: # 해당 점수 만드는데 필요한 화살 수가 n보다 작은 경우 : 나머지 화살을 0점에 박아넣기
                tmp[10] = n - arrow_num
            win_case_targets.append(tmp)

        #* 각 과녁판을 낮은 점수를 많이 맞춘 순으로 정렬하기 위해 정수 형태로 변경해서 정렬
        win_case_targets.sort(key = lambda r : int("1" + "".join(str(rr) for rr in r)))
        return win_case_targets[0]
    else:
        return [-1]