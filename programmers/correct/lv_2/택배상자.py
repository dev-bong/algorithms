from collections import deque

def solution(order):
    main_container = deque([i for i in range(1, len(order) + 1)]) # queue : 메인 컨테이너
    sub_container = [] # stack : 서버 컨테이너
    box_num = len(order)
    order = deque(order)

    while True:
        main_front = main_container[0] if main_container else None
        sub_top = sub_container[-1] if sub_container else None

        if not order: # 트럭으로 다 실었으면
            break
        if main_front == order[0]: # 메인 컨테이너에서 바로 트럭으로
            main_container.popleft()
            order.popleft()
        else:
            if sub_top == order[0]: # 서브 컨테이너에서 트럭으로
                sub_container.pop()
                order.popleft()
            else: # 메인 컨테이너에서 서브 컨테이너로
                if not main_container: # 더이상 트럭으로 실을 수 없을 때
                    break
                item = main_container.popleft()
                sub_container.append(item)

    return box_num - len(order)