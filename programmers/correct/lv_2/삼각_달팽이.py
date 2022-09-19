def make_sub_tri(size, start_num):
    # 테두리만 채우는 한 변이 n인 삼각형 만들기
    tri = [[] for i in range(size + 1)]
    num = start_num

    for i in range(1, size): # 왼쪽 변 채우기
        tri[i].append(num)
        num += 1
    
    for i in range(size): # 아래쪽 변 채우기
        tri[size].append(num)
        num += 1

    for i in range(size - 1, 1, -1): # 오른쪽 변 채우기
        tri[i].append(num)
        num += 1
    
    return (tri, num)

def push_center(arr, item): # item 리스트를 arr 중간에 삽입
    return arr[:len(arr)//2] + item + arr[len(arr)//2:]

def solution(n):
    answer = []
    triangle = [[] for i in range(n + 1)]
    end_num = 1
    push_idx = 1

    while True:
        sub_t, end_num = make_sub_tri(n, end_num) # sub_triangle 구하고

        for i in range(1, len(sub_t)): # push_idx 위치부터 삽입
            triangle[push_idx + i - 1] = push_center(triangle[push_idx + i - 1], sub_t[i])

        if n <= 3:
            break
        n -= 3
        push_idx += 2
    
    # for t in triangle:
    #     answer += t
    # return answer
    return sum(triangle, []) #! 다시보기

"""
1. make_sub_tri(n, 1)를 통해 테두리만 채우는 한변이 n개인 삼각형을 만들고
n > 3일 경우 그 중앙을 채울 삼각형을 make_sub_tri(n - 3, end_num)으로 만들면 됨

2. 그 후 중앙을 채울 sub_triangle을 push_center를 통해 조립

1, 2를 반복..
triangle에 sub_triangle을 삽입하는 위치는 push_idx = 1, 3, 5, 7, 9...

#! sum(iterable, 시작값)
    - 위 처럼 sum 함수에는 시작값 파라미터가 존재하며 default = 0
    - iterable의 요소들이 리스트일 경우에 start에 []를 넣어서 리스트 덧셈을 할수 있음
"""