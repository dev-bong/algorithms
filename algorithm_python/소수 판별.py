def is_prime(num): # num이 소수인지 아닌지 판별. num은 1 이상의 자연수
    if num == 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: # 1 외에 약수가 하나라도 있으면 소수
            return False
    return True

def eratosthenes(num): # 자연수 num 이하의 모든 소수들을 찾는 함수
    total_nums = set([i for i in range(1, num + 1)]) # 1 부터 num 까지 전체 수 집합
    non_primes = set() # 합성수 집합
    visited = set() # 방문한 수들 중 

    # 1은 소수가 아님
    visited.add(1)
    non_primes.add(1)

    # 2는 소수. 2의 배수(짝수)들은 모두 소수가 아님
    visited.add(2)
    for n in range(3, num + 1):
        if n % 2 == 0:
            visited.add(n)
            non_primes.add(n)

    cur = 3
    while cur <= (num ** 0.5): # root(num)까지만 이용하면 됨 #? 이유?
        if cur in visited:
            cur += 1
            continue

        visited.add(cur)
        for n in range(cur + 2, num + 1, 2): # cur은 모두 홀수, 2칸씩 뛰며 홀수만 검사 (짝수는 위에서 지워짐)
            if n % cur == 0:
                visited.add(n)
                non_primes.add(n)

        cur += 1

    return total_nums - non_primes

print(eratosthenes(100))

# TODO : 에라토스테네스 체 시간복잡도?? 더 개선 가능한가??