from itertools import permutations

def solution(user_id, banned_id):
    answer = set()
    uid_sets = []
    bid_sets = []
    uid_bid_match = {i : [] for i in range(len(banned_id))}

    # banned_id들과 match 검사하기위해서 (알파벳, 인덱스) 형태로 구성된 집합 만들기
    for uid in user_id:
        tmp = set()
        for i in range(len(uid)):
            tmp.add((uid[i], i))
        uid_sets.append(tmp)

    # user_id들과 match 검사하기위해서 (알파벳, 인덱스) 형태로 구성된 집합 만들기
    for bid in banned_id:
        tmp = set()
        for i in range(len(bid)):
            if bid[i] == "*":
                continue
            tmp.add((bid[i], i))
        bid_sets.append((tmp, len(bid)))
    
    # uid_sets와 bid_sets 간에 match 검사
    for i in range(len(uid_sets)):
        for j in range(len(bid_sets)):
            bids, blen = bid_sets[j]
            if len(uid_sets[i]) != blen: # 일단 길이가 같아야함
                continue

            if not bids - (uid_sets[i] & bids): # bids가 uids의 부분집합일 경우
                uid_bid_match[j].append(i)

    cases = permutations([i for i in range(len(user_id))], len(banned_id))
    for case in cases:
        is_match = True
        for i in range(len(case)):
            if case[i] not in uid_bid_match[i]:
                is_match = False
                break
        if is_match:
            answer.add(tuple(sorted(list(case))))

    return len(answer)