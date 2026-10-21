def solution(numbers, target):
    
    answer= [0]
    
    for number in numbers:
        temp = []
        for x in answer:
            temp.append(x + number)
            temp.append(x - number)
        answer = temp
        
    return answer.count(target)