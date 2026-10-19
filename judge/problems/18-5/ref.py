# 저자 풀이(위상 정렬)와 동일한 결과를 내는 빠른 버전
# 모든 팀 쌍 사이에 방향이 정해진 그래프(토너먼트)는 "각 팀이 이기는 팀 수"가 모두 다를 때만
# 사이클이 없고, 이때 위상 정렬 결과는 유일하다. (그래서 "?"가 나오는 경우는 생기지 않는다.)
import sys
data = sys.stdin.buffer.read().split()
p = 0
T = int(data[p]); p += 1
out = []
for _ in range(T):
    n = int(data[p]); p += 1
    last = data[p:p + n]; p += n
    pos = [0] * (n + 1)
    score = [0] * (n + 1)  # 자신보다 순위가 낮은 팀의 수
    for i, t in enumerate(last):
        t = int(t)
        pos[t] = i
        score[t] = n - 1 - i
    m = int(data[p]); p += 1
    for _ in range(m):
        a = int(data[p]); b = int(data[p + 1]); p += 2
        if pos[a] < pos[b]:  # 작년에는 a가 b보다 높았음 -> 뒤집힘
            score[a] -= 1
            score[b] += 1
        else:
            score[a] += 1
            score[b] -= 1
    rank = [0] * n
    ok = True
    for t in range(1, n + 1):
        s = score[t]
        if rank[n - 1 - s]:
            ok = False
            break
        rank[n - 1 - s] = t
    if ok:
        out.append(" ".join(map(str, rank)))
    else:
        out.append("IMPOSSIBLE")
print("\n".join(out))
