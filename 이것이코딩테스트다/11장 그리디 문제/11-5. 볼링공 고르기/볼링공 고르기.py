from itertools import combinations

def solution(n, m, k):
    answer = 0

    for a, b in combinations(range(n), 2):
        if k[a] != k[b]:
            answer += 1

    return answer
