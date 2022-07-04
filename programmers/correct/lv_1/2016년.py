def solution(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    yoil = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    total_days = 0

    for i in range(a-1):
        total_days += months[i]
    total_days += b

    return yoil[(total_days % 7)-1]