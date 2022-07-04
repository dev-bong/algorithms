def solution(price, money, count):
    total_price = 0
    mul_count = sum([i for i in range(1, count+1)]) #? 이렇게 말고 등차수열의 합 공식으로..
    
    total_price = price * mul_count
    
    if total_price > money:
        return total_price - money
    else:
        return 0