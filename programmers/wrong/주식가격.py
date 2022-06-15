def lower_list(li, num):
    idx = -1
    for l in li:
        if num < l:
            idx = li.index(l)
            break
    return li[:idx] if not idx == -1 else li

def solution(prices):
    length = len(prices)
    answer = [0] * length
    poped = []
    poped_min = 0
    price_idx = {}
    
    i = 1
    while prices:
        pop_item = prices[-1]

        if poped:
            if pop_item <= poped_min:
                answer[-i] = len(poped)
                poped = [pop_item] + poped
                poped_min = pop_item
                price_idx[pop_item] = i
            else:
                cnt = 0
                key_list = list(price_idx.keys())
                key_list = sorted(key_list)
                key_list = lower_list(key_list, pop_item)
                lower_price_idxs = [price_idx[key] for key in key_list]
                most_left_idx = max(lower_price_idxs)

                # for pp in poped: # 이부분 고치기!!
                #     """
                #     그 poped를 딕셔너리 식으로해서 key=price값, value=같은 price값중에 왼쪽에서 제일 가까운 인덱스..
                #     """
                #     cnt += 1
                #     if pop_item > pp:
                #         break
                answer[-i] = i - most_left_idx
                poped = [pop_item] + poped
                price_idx[pop_item] = i
        else:
            poped.append(pop_item)
            poped_min = pop_item
            answer[-1] = 0
            price_idx[pop_item] = i

        prices = prices[:-1]
        i += 1

    return answer

p = [1, 2, 3, 4, 2, 1, 3]

print(solution(p))

# ll = [1,3]
# n = 2
# print(lower_list(ll, n))