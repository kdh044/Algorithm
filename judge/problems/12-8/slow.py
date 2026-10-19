# 시작점 x 친구 순열마다 외벽을 한 칸씩 직접 칠해 보며 확인하는 풀이
# O(len(weak) * len(dist)! * (n + 이동 거리 합)) -> 저자 풀이보다 한 단계 느림
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    weak2 = weak + [w + n for w in weak]
    answer = len(dist) + 1
    for start in range(length):
        for friends in permutations(dist, len(dist)):
            checked = [False] * (2 * n + 101)  # 원형을 두 바퀴로 편 외벽
            i = start
            used = 0
            for f in friends:
                used += 1
                s = weak2[i]
                for p in range(s, s + f + 1):  # 친구가 지나가는 칸을 전부 칠함
                    checked[p] = True
                while i < start + length and checked[weak2[i]]:
                    i += 1
                if i == start + length:
                    answer = min(answer, used)
                    break
    if answer > len(dist):
        return -1
    return answer
