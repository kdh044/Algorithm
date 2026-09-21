from collections import deque

def solution(priorities, location):
    queue = deque(enumerate(priorities))
    answer = 0
    
    while queue:
        index, now = queue.popleft()
        
        if queue and now < max(p for i, p in queue):
            queue.append((index,now))
        else:
            answer += 1
            if index == location:
                return answer