import heapq

def solution(scoville, K):
    answer = 0
    h = []
    for sc in scoville: # 스코빌지수 힙에 넣기
        heapq.heappush(h, sc)

    while True:
        if len(h) == 1:
            return -1

        # 안매운 음식 2개 꺼내서 섞고 다시 넣기
        food1 = heapq.heappop(h)
        food2 = heapq.heappop(h)
        new_food = food1 + food2 * 2
        heapq.heappush(h, new_food)
        answer += 1

        if h[0] >= K:
            break

    return answer

##### heap 직접 구현해서 풀이 #####
"""
1. heapq 라이브러리 안쓰고
    - 정확도 검사는 다 맞는데 효율성에서 털린다
    - 이미 구현된 우선순위 큐 라이브러리를 이용하면 효율적으로 풀 수 있다고 명시되어있긴함..
    - 그래도 욕심이 나지만 다른사람들도 다 실패한 듯 하다

2. heapify 이용해보기
"""
class Heap():
    def __init__(self):
        self.heap_tree = []

    def root(self):
        return self.heap_tree[0] if len(self.heap_tree) else None

    def get_child_idx(self, idx):
        l_child = (idx * 2) + 1
        r_child = l_child + 1
        end_idx = len(self.heap_tree) - 1
        res =  (l_child if l_child <= end_idx else -1, r_child if r_child <= end_idx else -1)
        return res if res != (-1, -1) else None
    
    def get_parent_idx(self, idx):
        return -1 if idx == 0 else int((idx - 1) / 2)

    def swap(self, idx1, idx2):
        tmp = self.heap_tree[idx1]
        self.heap_tree[idx1] = self.heap_tree[idx2]
        self.heap_tree[idx2] = tmp

    def insertion(self, item):
        self.heap_tree.append(item)
        item_idx = len(self.heap_tree) - 1
        parent_idx = self.get_parent_idx(item_idx)

        while parent_idx >= 0:
            if self.heap_tree[parent_idx] > self.heap_tree[item_idx]:
                self.swap(parent_idx, item_idx)
                item_idx = parent_idx
                parent_idx = self.get_parent_idx(item_idx)
            else:
                break
    
    def deletion(self):
        if len(self.heap_tree) == 0:
            print("heap tree is empty!")
            return
        res = self.heap_tree[0]
        last_item = self.heap_tree[-1]
        self.heap_tree[0] = last_item
        self.heap_tree = self.heap_tree[:-1]

        item_idx = 0
        child_idxs = self.get_child_idx(item_idx)

        while child_idxs:
            l_child, r_child = child_idxs
            swap_candidate = []

            if l_child != -1 and self.heap_tree[item_idx] > self.heap_tree[l_child]:
                swap_candidate.append((l_child, self.heap_tree[l_child]))
            if r_child != -1 and self.heap_tree[item_idx] > self.heap_tree[r_child]:
                swap_candidate.append((r_child, self.heap_tree[r_child]))

            if swap_candidate:
                swap_candidate.sort(key=lambda r:r[1])
                swap_idx = swap_candidate[0][0]
                self.swap(item_idx, swap_idx)
                item_idx = swap_idx
                child_idxs = self.get_child_idx(item_idx)
            else:
                break
        
        return res

def solution(scoville, K):
    answer = 0
    h = Heap()
    for sc in scoville:
        h.insertion(sc)

    while True:
        if h.root() >= K:
            break

        if len(h.heap_tree) == 1:
            return -1
        
        food1 = h.deletion()
        food2 = h.deletion()
        new_food = food1 + food2 * 2
        h.insertion(new_food)
        answer += 1

    return answer