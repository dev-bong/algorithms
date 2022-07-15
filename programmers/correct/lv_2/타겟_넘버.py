class Node():
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

RES = []

def make_tree(node, remains, idx): # 트리 만들기
    if len(remains) > idx:
        dequeue_num = remains[idx]
        node.left = Node(node.item + dequeue_num)
        node.right = Node(node.item - dequeue_num)
        make_tree(node.left, remains, idx + 1)
        make_tree(node.right, remains, idx + 1)
    else:
        RES.append(node.item) # 리프노드(최종 계산 결과) 저장
        return

def solution(numbers, target):
    """
    0에서 시작해 numbers의 첫 숫자부터 +,- 두가지 연산으로 더해간다고 하면
    트리를 만들 경우 꽉찬 정삼각형 트리가 됨
    - 리프 노드의 개수는 2 ** len(numbers)
    - 리프 노드들(최종 계산 결과들)만 검사하면 됨
    """
    answer = 0
    nd = Node(0)
    make_tree(nd, numbers, 0)

    for r in RES:
        if r == target:
            answer += 1

    return answer

"""
! passed by assignment 주의 (아래처럼 코딩 X)
- remains로는 list가 전달 되는데 mutable이라서 call by assignment 처럼 동작하게 됨
- 그래서 재귀의 하위 분기로 갔다가 돌아오면 remains가 내가 예상한 상태가 아님
- mutable 변수를 변화시켜가면서 그것을 기준으로 삼는 재귀는 하지말도록!

def make_tree(node, remains): # 트리 만들기
    if remains:
        dequeue_num = remains.pop(0)
        node.left = Node(node.item + dequeue_num)
        node.right = Node(node.item - dequeue_num)
        make_tree(node.left, remains)
        make_tree(node.right, remains)
    else:
        RES.append(node.item)
        return
"""

# bfs, dfs 풀이 결과 위 풀이보다 성능 up
##### bfs 이용한 풀이 #####

from collections import deque
"""
그냥 리스트로 queue를 사용하게 되면 
    queue.pop(0) 이런 식으로 사용하게 되는데
    파이썬 list의 경우 stack에 가까워서?? pop(0)는 O(N)임
반면에 deque의 queue.popleft()는 O(1)

그래서 리스트로 했을땐 테스트케이스 1,2가 시간초과였는데
deque 쓰니까 가볍게 통과

어차피 재방문할 일이 없어서? visited 없어도 됨
"""

def solution(numbers, target):
    answer = 0
    queue = deque([(0, -1)]) # 옆에 -1은 numbers에서 index를 의미 (0보다 전)
    len_num = len(numbers)

    while queue:
        num, cur_idx = queue.popleft()
        if cur_idx == len_num - 1: # 리프노드? 중에
            if num == target: # 조건에 맞는 답 찾으면 답 개수 +1
                answer += 1
            continue
        next_num1, next_num2 = (num + numbers[cur_idx+1], num - numbers[cur_idx+1])
        queue.append((next_num1, cur_idx+1))
        queue.append((next_num2, cur_idx+1))

    return answer

##### dfs 이용한 풀이 #####

def solution(numbers, target):
    answer = 0
    stack = [(0, -1)]
    len_num = len(numbers)

    while stack:
        num, cur_idx = stack.pop()
        if cur_idx == len_num - 1:
            if num == target:
                answer += 1
            continue
        next_num1, next_num2 = (num + numbers[cur_idx+1], num - numbers[cur_idx+1])
        stack.append((next_num1, cur_idx+1))
        stack.append((next_num2, cur_idx+1))

    return answer