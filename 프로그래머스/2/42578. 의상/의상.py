def solution(clothes):
    c_dict = {}
    
    for _ , c in clothes:
        if c in c_dict:
            c_dict[c] += 1
        else:
            c_dict[c] = 1
            
    answer = 1
    
    for count in c_dict.values():
        answer *= count + 1
    
    return answer - 1 