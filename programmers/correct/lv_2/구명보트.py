from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people) # 시간 단축을 위한 deque 사용

    while people:
        answer += 1

        if len(people) == 1:
            break

        top = people.pop()
        bot_idx = 0

        if (top + people[bot_idx]) <= limit:
            people.popleft()
                
    return answer

"""
기존 알고리즘
1. 남은 사람 중 가장 무거운 사람 pick
2. 남은 사람 중 가장 가벼운 사람 pick
3. 두 사람 몸무게 합을 limit와 비교
    1. limit 보다 크면
        - 무거운 사람 혼자 타고 감
    2. limit 와 같으면 # ! 같거나 작으면 으로 수정해야함
        - 둘이 보트 타고 감
    3. limit 보다 작으면
        - 가벼운 사람 중 조건을 만족하는 제일 무거운 사람 찾아서 둘이 타고 감

* 개선점
* 1. deque 사용
*   - list의 pop(0)는 O(N)이고, deque의 popleft()는 O(1)


* 2. 기존 알고리즘의 3-3 과정 삭제
*   A <= B <= C <= D 일때 (A, B, C, D는 몸무게), B + D <= limit 이면..
*   B, D를 고르는 것이 최선이라 생각했으니 아니었음

*   기존 내 알고리즘 일때는 (B, D), (A, C)를 고르게 되고
*   수정된 알고리즘에서는 (A, D), (B, C)를 고르게 된다
*   수정된 알고리즘에서 (B, C) > limit 인 경우가 발생할 수 있을거라 생각했지만 부등식을 계산해보면 그런 경우는 발생하지 않음
"""