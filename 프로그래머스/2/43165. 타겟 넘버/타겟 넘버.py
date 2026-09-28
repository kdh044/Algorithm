from itertools import product

def solution(numbers, target):
    answer = 0

    for signs in product([1, -1], repeat=len(numbers)):
        total = 0

        for num, sign in zip(numbers, signs):
            total += num * sign

        if total == target:
            answer += 1

    return answer