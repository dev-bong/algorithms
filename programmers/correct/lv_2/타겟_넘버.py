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

# TODO : dfs, bfs로 간단히 풀어보기?? (근데 위 풀이도 dfs?느낌아닌가)