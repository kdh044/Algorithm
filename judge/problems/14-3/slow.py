# 스테이지마다 모든 사용자를 파이썬 반복문으로 직접 세는 O(N * M) 풀이
def solution(N, stages):
    answer = []
    for i in range(1, N + 1):
        reached = 0
        stay = 0
        for s in stages:
            if s >= i:
                reached += 1
                if s == i:
                    stay += 1
        fail = stay / reached if reached else 0
        answer.append((i, fail))
    answer.sort(key=lambda t: t[1], reverse=True)
    return [i for i, _ in answer]
