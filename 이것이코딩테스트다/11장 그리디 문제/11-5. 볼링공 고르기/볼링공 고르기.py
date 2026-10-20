def solution(n, m, k):
    answer = 0 
    for i in range(1, n):
        for j in range(i):
            if k[i] != k[j]:
                answer += 1
    return answer
