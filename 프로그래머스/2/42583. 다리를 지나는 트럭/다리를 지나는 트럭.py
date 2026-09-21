from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    waiting = deque(truck_weights)
    answer = 0

    while waiting:
        answer += 1

        bridge.popleft()

        if sum(bridge) + waiting[0] <= weight:
            bridge.append(waiting.popleft())
        else:
            bridge.append(0)

    return answer + bridge_length