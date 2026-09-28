def solution(numbers, target):
    result = [0]
    
    for number in numbers:
        temp = []
        for x in result:
            temp.append(x + number)
            temp.append(x - number)
        result = temp
        
    return result.count(target)