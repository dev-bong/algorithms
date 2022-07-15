def search(tickets, history, t_num, res):
    """
    history는 어떤 순서로 티겟들을 써서 여기까지 왔는지 저장 (ticket의 index들을 모은 문자열)
    - 문자열로 한 이유는 call by value 처럼 동작하기 위해서
    """
    his = [int(h) for h in history]
    if t_num == len(his): # 모든 항공권을 소모한 경우 저장
        res.append(history)
    for i in range(t_num):
        if i not in his: # 사용하지 않은 티켓 중에서..
            cur = tickets[his[-1]][1] if his else "ICN" # his가 없는 경우(출발 시)에는 "ICN" 부터
            arr = tickets[i][0]
            if cur == arr: # history의 마지막 티켓 도착지와 다음 티켓 출발지가 일치하는 경우
                search(tickets, history + str(i), t_num, res)



def solution(tickets):
    tickets_num = len(tickets)
    res = []
    routes = []

    search(tickets, "", tickets_num, res)

    for r in res:
        tmp = ""
        for idx in r:
            tmp += tickets[int(idx)][0] + " "
        tmp += tickets[int(idx)][1]
        routes.append(tmp)
    
    routes.sort()

    return routes[0].split(" ")

"""
dfs나 bfs로 풀라고 만든 문제인 것 같으나 처음에 dfs로 풀다가 잘 안되서 이렇게 품
- 이것도 dfs? 인거 같기도??
- 기존에 쓰던 stack을 이용한 dfs를 쓰면 route를 하나만 찾는데 visited를 추가해가면서 여러번 돌려서 모든 route를 찾는 식으로 구현했으나 잘 안됨

위 풀이 테스트케이스 1번만 안됨
- 런타임 에러가 뜨는데 routes가 빈 배열로 되어서 마지막 리턴할 때 index error가 뜨는거 같음
- 중복티켓인 경우가 문제라고 해서 좀 수정했었는데 소용없었음..
"""