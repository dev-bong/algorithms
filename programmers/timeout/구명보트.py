def solution(people, limit):
    answer = 0
    people.sort() # 몸무게 순 정렬

    while people:
        if len(people) == 1:
            answer += 1
            break

        top = people.pop() # 남은 사람 중 가장 무거운 사람
        bot_idx = 0

        if (top + people[bot_idx]) == limit: # 무거운사람 + 가벼운사람이 딱 limit -> 둘이 보트
            people.pop(0)
        elif (top + people[bot_idx]) < limit: # 조건을 만족하는 가벼운사람 중 제일 무거운 사람 찾기
            for i in range(1, len(people)):
                if (top + people[i]) > limit:
                    break
                else:
                    bot_idx = i
            people.pop(bot_idx)
        
        answer += 1
                
    return answer

"""
1. 남은 사람 중 가장 무거운 사람 pick
2. 남은 사람 중 가장 가벼운 사람 pick
3. 두 사람 몸무게 합을 limit와 비교
    1. limit 보다 크면
        - 무거운 사람 혼자 타고 감
    2. limit 와 같으면
        - 둘이 보트 타고 감
    3. limit 보다 작으면
        - 가벼운 사람 중 조건을 만족하는 제일 무거운 사람 찾아서 둘이 타고 감

효율성 테스트 1, 3 통과 X
"""