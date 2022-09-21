def solution(info, query):
    answer = [0 for i in range(len(query))]
    info_list = [info[i].split(" ") for i in range(len(info))]
    query_list = []

    for i in range(len(query)):
        lang, part, career, remain = query[i].split(" and ")
        food, score = remain.split(" ")
        query_list.append([lang, part, career, food, score])

    for il in info_list:
        for i in range(len(query_list)):
            if query_list[i][0] not in [il[0], "-"]:
                continue
            if query_list[i][1] not in [il[1], "-"]:
                continue
            if query_list[i][2] not in [il[2], "-"]:
                continue
            if query_list[i][3] not in [il[3], "-"]:
                continue
            if int(il[4]) < int(query_list[i][4]):
                continue
            answer[i] += 1

    return answer