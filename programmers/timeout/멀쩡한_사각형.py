def gcd(a, b): # 최대공약수
    small = min([a, b])
    for i in range(small, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def solution(w,h):
    total_square = w * h
    inc = h / w # 기울기
    g = gcd(w, h)
    rmv_square = 0
    wg = w // g
    
    for i in range(1, wg + 1): # i는 x좌표 (무조건 정수)
        ex_y = inc * (i - 1) # 한칸 전 y좌표
        cur_y = inc * i # 현재 y 좌표
        floor_ex = int(ex_y)
        ceil_cur = int(cur_y) if int(cur_y) == cur_y else int(cur_y) + 1
        rmv = ceil_cur - floor_ex
        rmv_square += rmv # 한칸씩 이동하며 제거되는 사각형 계산
    
    rmv_square *= g

    return total_square - rmv_square

"""
테케 11 시간초과
"""