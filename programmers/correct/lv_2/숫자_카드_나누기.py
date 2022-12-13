def pick_candidate(a1, a2):
    min_a1 = a1[0]
    res = []

    #* a1의 공약수 구하기
    for i in range(1, int(min_a1 ** 0.5) + 1):
        cand = [min_a1 // i, i]
        for c in cand:
            is_cf = True
            for a in a1:
                if a % c != 0:
                    is_cf = False
                    break
            if is_cf:
                #* a1의 공약수이면서 a2의 수들의 약수가 아닌 수만 res에 넣기
                is_div = False
                for b in a2:
                    if b % c == 0:
                        is_div = True
                        break
                if not is_div:
                    res.append(c)
    return max(res) if res else 0

def solution(arrayA, arrayB):
    arrayA.sort()
    arrayB.sort()
    candidate = []

    candidate.append(pick_candidate(arrayA, arrayB))
    candidate.append(pick_candidate(arrayB, arrayA))
   
    return max(candidate)