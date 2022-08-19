def solution(routes):
    answer = 0

    while routes:
        routes.sort(key = lambda r : r[0]) # 진입 순으로 정렬
        route = routes.pop() # 진입이 가장 늦은 차량 선택
        camera = route[0] # 해당 차량 진입 시점에 카메라 세우기
        answer += 1
        
        routes.sort(key = lambda r : r[1]) # 탈출 순으로 정렬
        while routes: # 탈출 시점이 카메라 시점보다 늦은 경우 모두 pop
            st, end = routes[-1]
            if camera <= end:
                routes.pop()
            else:
                break

    return answer

# TODO : 반복할때마다 정렬을 2번씩해서 좀 비효율적인 것 같음. 수정해보기