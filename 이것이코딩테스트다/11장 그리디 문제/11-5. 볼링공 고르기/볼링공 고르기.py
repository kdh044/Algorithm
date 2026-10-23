from collections import Counter

def solution(n, m, k):
    count = Counter(k)
    answer = 0
    remain = n

    for weight in sorted(count):
        remain -= count[weight]
        answer += count[weight] * remain

    return answer
