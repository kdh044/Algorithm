def solution(name):
    answer = 0
    
    for alpha in name:
        up = ord(alpha) - ord("A")
        down = ord("Z") - ord(alpha) + 1
        
        if up >= down:
            answer += down
        else:
            answer += up
            
    n = len(name)
    move = n - 1
    
    for i in range(n):
        next_idx = i + 1
        
        while next_idx < n and name[next_idx] == "A":
            next_idx += 1

        right_first = 2 * i + (n - next_idx)

        left_first = i + 2 * (n - next_idx)

        move = min(move, right_first, left_first)

    return answer + move