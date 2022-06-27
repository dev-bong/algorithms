def solution(nums):
    num_pmon = len(nums) # 폰켓몬 전체 수
    pick_pmon = num_pmon // 2
    types_pmon = len(list(set(nums))) # 폰켓몬 종류 수

    return pick_pmon if types_pmon >= pick_pmon else types_pmon