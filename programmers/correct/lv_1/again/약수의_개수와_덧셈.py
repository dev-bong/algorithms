def factor_num(num): # 약수 개수
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    return cnt

def solution(left, right):
    answer = 0

    for num in range(left, right + 1):
        f_cnt = factor_num(num)
        if f_cnt % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer

#? 제곱수의 약수는 홀수개???
"""
(A**i) * (B**j)
>> 약수의 개수 = (i + 1) * (j + 1)
제곱수의 경우 i, j가 모두 짝수이므로 약수의 개수 = 홀수 * 홀수 가 됨

제곱수가 아니어도 약수의 개수가 홀수일 수 있나???
- 그럴수없음
- 짝수*짝수, 짝수*홀수 모두 결과는 짝수이기 때문에
- 소인수분해 결과에서 인수의 지수가 모두 짝수여야함 = 제곱수
"""