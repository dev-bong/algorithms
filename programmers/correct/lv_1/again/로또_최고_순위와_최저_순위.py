def solution(lottos, win_nums):
    zeros = 0
    correct_num = 0

    for lotto in lottos:
        if lotto in win_nums:
            correct_num += 1
        elif lotto == 0:
            zeros += 1

    # 1개 이하로 맞추면 똑같이 6등이라서 7등, 0등같은 순위가 나오는것 방지
    now_rank = min(6 - correct_num + 1, 6)
    max_rank = max(now_rank - zeros, 1)
    return [max_rank, now_rank]