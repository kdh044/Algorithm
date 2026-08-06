def solution(clothes):
    count = {}

    for name, category in clothes:
        if category not in count:
            count[category] = 0

        count[category] += 1

    answer = 1

    for clothing_count in count.values():
        answer *= clothing_count + 1

    return answer - 1