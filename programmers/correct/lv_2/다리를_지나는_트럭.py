def on_bridge_weight(on_bridge): # 다리 위 트럭들 무게 총합
    total_weight = 0
    for ob in on_bridge:
        if not ob[1] == 0:
            total_weight += ob[0]
    return total_weight

def solution(bridge_length, weight, truck_weights):
    time = 0
    on_bridge = []

    while True:
        finished_trucks = 0
        for ob in on_bridge:
            if not ob[1] == 0:
                ob[1] -= 1
            else:
                finished_trucks += 1
        on_bridge = on_bridge[finished_trucks:] # 다리 다 건넌 트럭들 제거

        if not on_bridge and not truck_weights:
            break

        if truck_weights:
            tw = truck_weights[0]
            if (tw + on_bridge_weight(on_bridge)) > weight:
                pass
            else:
                on_bridge.append([tw, bridge_length])
                truck_weights = truck_weights[1:]

        time += 1

    return time