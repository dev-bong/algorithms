def gcd(a, b): # 최대공약수
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def solution(w,h):
    total_square = w * h

    #! w, h 중 작은쪽을 w로 설정하여 작은쪽으로 반복문 돌도록 하여 시간 줄이기
    wh = [w, h]
    wh.sort()
    w = wh[0]
    h = wh[1]

    inc = h / w # 기울기
    g = gcd(w, h)
    rmv_square = 0
    wg = w // g
    
    for i in range(1, wg + 1): # i는 x좌표 (무조건 정수)
        ex = inc * (i - 1) # 한칸 전 y좌표
        cur = inc * i # 현재 y 좌표
        floor_ex = int(ex)
        ceil_cur = int(cur) if int(cur) == cur else int(cur) + 1
        rmv = ceil_cur - floor_ex
        rmv_square += rmv # 한칸씩 이동하며 제거되는 사각형 계산
    
    rmv_square *= g

    return total_square - rmv_square

"""
0. 평면 좌표라고 생각

1. 최대공약수 이용
    최대공약수를 계산하면 직선에서 x, y 좌표 모두 정수인 좌표를 구할 수 있음
    패턴은 반복되므로 문제의 사이즈를 줄일 수 있음

2. 제거되는 사각형 계산
    직선이 지나가면서 (1, 2.xxx)를 지나간다고 하면 (x 좌표는 정수로 고정)
    (1, 2) ~ (1, 3)을 변으로 하는 사각형은 못쓰게 됨
    이에 따라 직선이 (1, a), (2, b)를 지난다고 하면
    그 회차에 제거되는 사각형은 ceil(b) - floor(a) 로 구할 수 있음

======= 이전 풀이 ========

3. 시간초과 해결
    w랑 h 중 작은쪽으로 반복문 돌리는 방법으로 테케 11번 시간초과는 해결했으나
    뜬금없이 테케 4, 17이 실패함

    찾아보니 부동소수점 오류인것 같음 ..

아래가 정답

4. 부동소수점 오류 해결??
    소수인 상태로 계산하는 부분을 없앰
    몫과 나머지를 이용하여 계산
"""

def gcd(a, b): # 최대공약수
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def solution(w,h):
    total_square = w * h

    #! 시간 감축
    wh = [w, h]
    wh.sort()
    w = wh[0]
    h = wh[1]

    g = gcd(w, h)
    rmv_square = 0
    hg = h // g
    wg = w // g
    
    for i in range(1, wg + 1):
        if i - 1 == 0:
            floor_ex = 0
        else:
            floor_ex = (hg * (i - 1)) // wg
        ceil_cur = (hg * i) // wg
        if (hg * i) % wg != 0:
            ceil_cur += 1
        rmv = ceil_cur - floor_ex
        rmv_square += rmv
    
    rmv_square *= g

    return total_square - rmv_square