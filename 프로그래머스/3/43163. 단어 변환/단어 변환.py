from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque()
    q.append((begin, 0))
    
    visited = set()
    visited.add(begin)
    
    while q:
        word, count = q.popleft()
        
        if word == target:
            return count
        
        for next_word in words:
            if next_word in visited:
                continue
            
            diff = 0
            
            for i in range(len(word)):
                if word[i] != next_word[i]:
                    diff += 1
            
            if diff == 1:
                visited.add(next_word)
                q.append((next_word, count + 1))
    
    return 0