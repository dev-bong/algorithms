def diff_words(word_len, word1, word2): # 같은 길이 문자 비교
    cnt = 0
    for i in range(word_len):
        if word1[i] != word2[i]:
            cnt += 1
    return cnt 

def solution(begin, target, words):
    word_len = len(begin)

    if target not in words:
        return 0
    
    # 필요한 최소 단계. 즉, 최단 경로를 찾는 문제이기 때문에 BFS 이용
    queue = [(begin, 0)]
    visited = set([begin])

    while queue:
        deq_item, step = queue.pop(0)

        if deq_item == target: # 목표에 도착하면 리턴
            return step

        for word in words:
            # 현재 단어와 1글자만 다른 단어로만 이동할 수 있음 + visited 체크
            if diff_words(word_len, word, deq_item) == 1 and word not in visited:
                queue.append((word, step + 1)) # 몇 단계 거쳤는지 추가로 저장
                visited.add(word)
    return 0