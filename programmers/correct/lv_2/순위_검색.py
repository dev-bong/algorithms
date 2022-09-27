def solution(info, query):
    answer = [0 for i in range(len(query))]
    attrs = {
        "lang" : ["cpp", "java", "python", "-"], # "-"는 해당 attr로 검색하지 않는 경우
        "part" : ["backend", "frontend", "-"],
        "career" : ["junior", "senior", "-"],
        "food" : ["chicken", "pizza", "-"]
    }
    info_dict = {}
    bit_4 = [bin(n)[2:] for n in range(16)] # 4자리 2진수로 4개의 attr들이 각각 선택되거나 선택되지 않는 경우 표현
    for i in range(len(bit_4)):
        num_0 = 4 - len(bit_4[i])
        bit_4[i] = ("0" * num_0) + bit_4[i]

    for lang in attrs["lang"]:
        for part in attrs["part"]:
            for career in attrs["career"]:
                for food in attrs["food"]:
                    info_dict[lang + part + career + food] = [] # 4개의 attr 조합해서 key 만들어놓기

    for i in range(len(info)):
        lang, part, career, food, score = info[i].split() # info에서 뽑기
        lang = [lang, "-"] if lang != "-" else ["-"]
        part = [part, "-"] if part != "-" else ["-"]
        career = [career, "-"] if career != "-" else ["-"]
        food = [food, "-"] if food != "-" else ["-"]

        for bit in bit_4: # attr 각각 들어가는 경우, 빠지는 경우 (ex> "cpp"가 있을 경우, "cpp"로도 검색 되어야하고 "-"로도 검색 되어야하기 때문)
            info_dict[lang[int(bit[0])] + part[int(bit[1])] + career[int(bit[2])] + food[int(bit[3])]].append(int(score))

    for key in info_dict:
        info_dict[key].sort() # 이진탐색을 하기 위해 정렬

    for i in range(len(query)):
        lang, part, career, remain = query[i].split(" and ")
        food, score = remain.split(" ")
        query_res = info_dict[lang + part + career + food] # 기록한 info_dict에서 query(key)에 맞는 score 리스트

        ## 이진탐색 ##
        l = len(query_res)
        tmp = l

        low, high = 0, l - 1

        while low <= high:
            mid = (low + high) // 2

            if int(score) <= query_res[mid]: # query score랑 정확히 일치할 필요 X, query score 이상인 score 중에 가장 작은 것을 찾는 것임
                tmp = mid
                high = mid - 1
            else:
                low = mid + 1

        answer[i] = l - tmp

    return answer