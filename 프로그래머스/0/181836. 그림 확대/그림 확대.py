def solution(picture, k):
    answer = []
    
    for row in picture:
        new_row = ""
        
        for x in row:
            new_row += x * k
        
        for _ in range(k):
            answer.append(new_row)
            
    return answer