from collections import deque

def solution(n, courses):
    answer = [0] * (n + 1)
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    time = [0] * (n + 1)
    
    for i, course in enumerate(courses,start = 1):
        time[i] = course[0]
        
        for pre in course[1:]:
            graph[pre].append(i)
            indegree[i] += 1
        
    q = deque()
    
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            answer[i] = time[i]
            
    while q:
        now = q.popleft()
        
        for next_course in graph[now]:
            indegree[next_course] -= 1
            
            answer[next_course] = max(answer[next_course], answer[now] + time[next_course])
            
            if indegree[next_course] == 0:
                q.append(next_course)
    return answer[1:]
