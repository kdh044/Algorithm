def solution(n, m, k):
    count = [0] * (m + 1)

    for weight in k:
        count[weight] += 1

    answer = n * (n - 1) // 2

    for i in range(1, m + 1):
        answer -= count[i] * (count[i] - 1) // 2

    return answer
