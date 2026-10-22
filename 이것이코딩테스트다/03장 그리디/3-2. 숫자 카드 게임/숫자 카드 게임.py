def solution(n, m, cards):
    answer = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(cards[i][j])
        temp.sort()
        answer.append(temp[0])
        
    answer.sort()      
    return answer[-1]
