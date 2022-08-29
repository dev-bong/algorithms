from collections import deque

def solution(n, words):
    words = deque(words) # popleft를 위해 deque 사용
    users = {i : 0 for i in range(1, n + 1)} # 사용자 번호 : 차례 (단어 말한 횟수)
    used_words = [] # 사용했던 단어들
    cur = 0

    while words:
        cur = (cur % n) + 1 # 돌아가면서 말하기
        cur_word = words.popleft()
        users[cur] += 1

        if used_words:
            ex_word = used_words[-1]
            if ex_word[-1] != cur_word[0] or cur_word in used_words: # 끝말잇기가 안되었거나, 이미 말했던 단어면 탈락!
                return [cur, users[cur]] # [탈락한 사용자 번호, 몇번째 차례에 탈락했는지]

        used_words.append(cur_word)
        
    return [0, 0] # 주어진 단어들로 탈락 결정이 안될 때