def solution(n, costs):
    answer = 0
    costs.sort(key = lambda r : r[2]) # edge들 cost 순으로 정렬
    conn = set() # edge로 연결된 섬들의 집합
    selected = set() # edge들 중 선택된 edge 인덱스 집합
    road_num = len(costs)

    # 초기화.. 가장 낮은 cost의 edge중 아무거나 넣기
    answer += costs[0][2]
    conn.update([costs[0][0], costs[0][1]])
    selected.add(0)

    while len(conn) < n:
        for i in range(road_num):
            if i in selected: # 선택된 edge는 패스
                continue
            island1, island2, cost = costs[i]
            island_set = set([island1, island2])

            if len(island_set - conn) == 1: # 해당 edge가 연결하는 섬 2개중 하나만 conn에 속하는 경우
                #! 섬1, 섬2 중 한개는 conn에 있어야 연결 가능함
                conn |= island_set - conn
                selected.add(i)
                answer += cost
                break

    return answer

"""
매 회차 cost 순으로 edge들을 순회하며 연결가능한 edge 연결

#! 섬1, 섬2 2개가 모두 conn에 없는 경우
    conn = {0, 1, 2, 3} 인데 (0, 1), (2, 3)으로 덩어리가 2개로 되는 경우가 있을 수 있음
    conn에 있는 섬들은 모두 한 덩어리로 묶여있어야함
"""