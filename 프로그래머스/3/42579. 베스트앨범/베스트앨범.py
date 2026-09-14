def solution(genres, plays): 
    answer = [] 
     
    dic1 = {} 
    dic2 = {} 
 
    for i, (g, p) in enumerate(zip(genres, plays)): 
        if g not in dic1: 
            dic1[g] = [(i, p)] 
        else: 
            dic1[g].append((i, p)) 
         
        if g not in dic2: 
            dic2[g] = p 
        else: 
            dic2[g] += p 
 
    for k, v in sorted(dic2.items(), key=lambda x: x[1], reverse=True): 
        # 재생수가 많은 노래부터, 같으면 고유번호가 작은 순서
        songs = sorted(dic1[k], key=lambda x: (-x[1], x[0]))   
         
        for i, p in songs[:2]: 
            answer.append(i)
            
    return answer