def search(tickets, history, t_num, res):
    """
    티켓을 모두 사용하는 경우들을 리턴 (하나의 경우는 티켓 인덱스의 나열로 표현)
    history는 어떤 순서로 티겟들을 써서 여기까지 왔는지 저장 (ticket의 index들을 모은 문자열)
    - 문자열로 한 이유는 call by value 처럼 동작하기 위해서
    """
    his = [int(h) for h in history.split(",")] if history else [] # ! 수정 포인트 1
    if t_num == len(his): # 모든 항공권을 소모한 경우 저장
        res.append(history)
    for i in range(t_num):
        if i not in his: # 사용하지 않은 티켓 중에서..
            cur = tickets[his[-1]][1] if his else "ICN" # his가 없는 경우(출발 시)에는 "ICN" 부터
            arr = tickets[i][0]
            if cur == arr: # history의 마지막 티켓 도착지와 다음 티켓 출발지가 일치하는 경우
                origin = history # ! 수정 포인트 2
                history = history + "," + str(i) if his else str(i)
                search(tickets, history, t_num, res)
                history = origin



def solution(tickets):
    tickets_num = len(tickets)
    res = []
    routes = []

    search(tickets, "", tickets_num, res)

    for r in res:
        tmp = ""
        for idx in r.split(","):
            tmp += tickets[int(idx)][0] + " "
        tmp += tickets[int(idx)][1]
        routes.append(tmp)
    routes.sort()

    return routes[0].split(" ")

"""
수정 포인트 1
- 기존 코드는 tickets 인덱스가 두자리가 되는 것을 고려하지 않았음
- 인덱스가 두자리가 될 경우 search의 결과로 제대로 파싱이 불가함
    ex> 11123 (1, 11, 23 / 11, 12, 3 / .. etc) 하나의 인덱스 나열로 여러가지 해석이 가능
- 인덱스 사이에 ","를 넣어주어 구분하도록 변경

수정 포인트 2
- 하나의 콜에서 여러개의 search를 호출할 경우 history의 변화가 의도와 달랐음
    ex> 현재 history = "1,4,5" 조건에 맞는 index = 0, 3, 7 일 경우
    의도는
        search(tickets, "1,4,5,0", t_num, res)
        search(tickets, "1,4,5,3", t_num, res)
        search(tickets, "1,4,5,7", t_num, res)
    하지만 실제 동작은
        search(tickets, "1,4,5,0", t_num, res)
        search(tickets, "1,4,5,0,3", t_num, res)
        search(tickets, "1,4,5,0,3,7", t_num, res)
- 위 예시 처럼 동작하는 것을 수정
"""

# TODO : DFS로 풀어보기 (아래는 전에 코드 짜다 만것)

# def solution(tickets):
#     routes = {}
#     num_tickets = len(tickets)

#     for tc in tickets:
#         if tc[0] in routes:
#             routes[tc[0]].append(tc[1])
#         else:
#             routes[tc[0]] = [tc[1]]

#     for route in routes:
#         routes[route].sort(reverse=True)
#     print(routes)
    
#     stack = ["ICN"]
#     visited = []
#     ex_item = ""

#     while stack:
#         item = stack.pop()
#         visited.append(item)
        
#         if item in routes:
#             if routes[item]:
#                 if routes[item][-1] in routes:
#                     stack.append(routes[item].pop())
#                 else:
#                     pass
#             else:
#                 break
#         else:
#             pass

#     return visited