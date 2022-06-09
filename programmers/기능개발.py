class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        dq_items = [self.queue[0]]
        dq_size = 1
        for item in self.queue[1:]:
            if dq_items[0] >= item:
                dq_items.append(item)
                dq_size += 1
            else:
                break

        self.queue = self.queue[dq_size:]
        return dq_items

    def is_empty(self):
        return False if self.queue else True

def solution(progs, speeds):
    remain_days = Queue()
    res = []

    for i in range(len(progs)):
        remain_prog = 100 - progs[i]
        remain_day = remain_prog // speeds[i] if remain_prog % speeds[i] == 0 else remain_prog // speeds[i] + 1
        remain_days.enqueue(remain_day)

    while True:
        if remain_days.is_empty():
            break
        dq = remain_days.dequeue()
        res.append(len(dq))
    return res