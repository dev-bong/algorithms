class Heap():
    def __init__(self):
        self.heap_tree = [] # 내가 짠거는 index 0도 사용

    def get_child_idx(self, idx): # child : 2*idx+1, 2*idx+2
        l_child = (idx * 2) + 1
        r_child = l_child + 1
        end_idx = len(self.heap_tree) - 1
        res =  (l_child if l_child <= end_idx else -1, r_child if r_child <= end_idx else -1)
        return res if res != (-1, -1) else None
    
    def get_parent_idx(self, idx): # parent : floor((idx-1)/2)
        return -1 if idx == 0 else int((idx - 1) / 2) # int가 floor 역할

    def swap(self, idx1, idx2): # 두 인덱스 값 스왑
        tmp = self.heap_tree[idx1]
        self.heap_tree[idx1] = self.heap_tree[idx2]
        self.heap_tree[idx2] = tmp

    def insertion(self, item): # 삽입
        self.heap_tree.append(item) # 가장 끝 자리에 신규 아이템 삽입
        item_idx = len(self.heap_tree) - 1
        parent_idx = self.get_parent_idx(item_idx)

        while parent_idx >= 0: # 부모 노드랑 비교하면서 규칙에 맞지 않으면 교환하면서 올라감
            if self.heap_tree[parent_idx] > self.heap_tree[item_idx]:
                self.swap(parent_idx, item_idx)
                item_idx = parent_idx
                parent_idx = self.get_parent_idx(item_idx)
            else:
                break
    
    def deletion(self): # 삭제
        if len(self.heap_tree) == 0:
            print("heap tree is empty!")
            return
        # 루트와 마지막노드 값을 바꾸고 마지막 노드 제거
        res = self.heap_tree[0]
        last_item = self.heap_tree[-1]
        self.heap_tree[0] = last_item
        self.heap_tree = self.heap_tree[:-1]

        item_idx = 0
        child_idxs = self.get_child_idx(item_idx)

        while child_idxs:
            l_child, r_child = child_idxs
            swap_candidate = []

            # 부모보다 작은 자식이 있으면 스왑후보에 넣기
            if l_child != -1 and self.heap_tree[item_idx] > self.heap_tree[l_child]:
                swap_candidate.append((l_child, self.heap_tree[l_child]))
            if r_child != -1 and self.heap_tree[item_idx] > self.heap_tree[r_child]:
                swap_candidate.append((r_child, self.heap_tree[r_child]))

            if swap_candidate:
                swap_candidate.sort(key=lambda r:r[1]) # 스왑 후보 중 더 작은값을 가진 자식이랑 스왑하기 위해 정렬
                swap_idx = swap_candidate[0][0]
                self.swap(item_idx, swap_idx)
                item_idx = swap_idx
                child_idxs = self.get_child_idx(item_idx)
            else:
                break
        
        return res