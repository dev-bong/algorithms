def solution(participant, completion):
    p_dict = {}

    for p in participant:
        if p in p_dict:
            p_dict[p][0] += 1
        else:
            p_dict[p] = [1,0]

    for c in completion:
        p_dict[c][1] += 1
    
    for pd in p_dict:
        if p_dict[pd][0] != p_dict[pd][1]:
            return pd