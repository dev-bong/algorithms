def solution(x, y, n):
    nums = set([x])

    for depth in range(1000001):
        next_nums = set()
        while nums:
            num = nums.pop()
            if num == y:
                return depth
            if (num + n) <= y:
                next_nums.add(num + n)
            if (num * 2) <= y:
                next_nums.add(num * 2)
            if (num * 3) <= y:
                next_nums.add(num * 3)
        if not next_nums:
            return -1
        nums = next_nums