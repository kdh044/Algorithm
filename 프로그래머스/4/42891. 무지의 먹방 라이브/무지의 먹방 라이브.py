import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    
    for i, time in enumerate(food_times, start = 1):
        heapq.heappush(q, (time, i))
    
    previous = 0
    length = len(food_times)
   
    while q:
        cost = (q[0][0] - previous) * length
        
        if k >= cost:
            length -= 1
            previous = heapq.heappop(q)[0]
            k -= cost
        else:
            break
        
    q.sort(key=lambda x: x[1])
        
    return q[k % length][1]