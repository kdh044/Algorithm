def solution(position):
    dx = [2,1,-1,-2,-2,-1,1,2]
    dy = [1,2,2,1,-1,-2,-2,-1]
    
    x = ord(position[0]) - ord('a') + 1
    y = int(position[1])
    answer = 0
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 < nx <= 8 and 0 < ny <= 8:
            answer += 1
            
    return answer
