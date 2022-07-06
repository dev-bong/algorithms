def total_time(history): # 총 시간 계산 (분 단위)
    if len(history) % 2 != 0: # history가 홀수면 마지막 출차 기록이 없다는 뜻
        history.append(60 * 24 - 1) # 23:59 까지의 시간 (분 단위)
    return sum(history)

def ceil_num(num): # 올림 함수
    int_num = int(num)
    return int_num + 1 if (num - int(num)) > 0 else int_num

def solution(fees, records):
    answer = []
    car_his = {}
    basic_time, basic_fee, unit_time, unit_fee = fees

    for record in records:
        time, car_num, in_out = record.split(" ")
        h, m = time.split(":")
        time_min = (int(h) * 60) + int(m) # 분 단위 시간 계산
        if in_out == "IN": time_min = -time_min # IN이면 -, OUT이면 +

        if car_num in car_his:
            car_his[car_num].append(time_min)
        else:
            car_his[car_num] = [time_min]
    
    car_nums = sorted(list(car_his.keys())) # 차량 번호 순서대로 정렬 (문자열 정렬)
    for c_num in car_nums:
        total_fee = 0
        tt = total_time(car_his[c_num])
        
        if tt <= basic_time:
            total_fee = basic_fee
        else:
            remain_time = tt - basic_time
            over_unit_time = ceil_num(remain_time / unit_time)
            total_fee = basic_fee + over_unit_time * unit_fee
        answer.append(total_fee)

    return answer