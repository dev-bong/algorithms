def solution(word):
    moem = ["0", "A", "E", "I", "O", "U"] # 사용가능한 모음들 + 빈칸
    dic = []

    for i in range(6): # 모든 경우의 수
        for j in range(6):
            for k in range(6):
                for l in range(6):
                    for m in range(6):
                        dic.append(moem[i] + moem[j] + moem[k] + moem[l] + moem[m])

    for i in range(len(dic)):
        dic[i] = dic[i].replace("0","") # 0을 빈칸으로
    
    dic = list(set(dic)) # 중복 지우기
    dic.sort()

    return dic.index(word)


##### 코드 개선 #####
def solution(word):
    moem = ["", "A", "E", "I", "O", "U"] # 빈칸을 "0"으로 하지 않고 그냥 ""로 하면 완성된 문자열에서 "0"을 지울 필요 없음
    dic = []

    for i in range(6):
        for j in range(6):
            for k in range(6):
                for l in range(6):
                    for m in range(6):
                        dic.append(moem[i] + moem[j] + moem[k] + moem[l] + moem[m])
    
    dic = list(set(dic))
    dic.sort()

    return dic.index(word)