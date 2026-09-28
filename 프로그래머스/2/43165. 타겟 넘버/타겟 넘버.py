def solution(numbers, target):
    result = [0]

    for num in numbers:
        temp = []

        for x in result:
            temp.append(x + num)
            temp.append(x - num)

        result = temp

    return result.count(target)