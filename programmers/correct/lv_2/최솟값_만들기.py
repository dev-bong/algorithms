def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer

"""
그냥 뭔가
최소값 * 최대값 + 그다음 작은값 * 그다음 큰값 ... 이런식으로 하면 될거 같았는데 진짜 됨
    큰수일수록 곱셈 후 크게 증가하므로, 큰수에는 작은수를 곱해줘야함

TODO : 수학적인 공식???
"""