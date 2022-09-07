from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque([]) # LRU

    if cacheSize == 0: # cacheSize가 0인 경우
        return len(cities) * 5

    for city in cities:
        city_l = city.lower()
        if city_l in cache: # cache hit
            answer += 1
            cache.remove(city_l)
            cache.append(city_l)
        else: # cache miss
            answer += 5
            if len(cache) < cacheSize: # cache가 다 차지 않았을 때
                cache.append(city_l)
            else: # cache가 가득 찼을 때
                cache.popleft()
                cache.append(city_l)
    return answer