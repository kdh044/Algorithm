def solution(array, commands):
    answer = []
    for command in commands:
        temp = []
        i = command[0]
        j = command[1]
        k = command[-1]
        temp = array[i - 1:j]
        temp.sort()
        answer.append(temp[k - 1])
    return answer