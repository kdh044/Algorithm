from collections import deque

def solution(priorities, location):
    queue = deque(enumerate(priorities))
    answer = 0
    
    while queue:
        index, prior = queue.popleft()
        if queue and prior < max(p for i,p in queue):
            queue.append((index,prior))
        else:
            answer += 1
            
            if index == location:
                return answer