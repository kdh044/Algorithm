# 저자 풀이(원형을 2배로 펼침 + 친구 순열 완전 탐색)와 같은 결과를 내는 더 빠른 풀이.
# 시작점마다, "사용한 친구 집합(비트마스크)"으로 앞에서부터 연속해서 점검할 수 있는
# 취약 지점 수의 최댓값을 DP로 구한다. (순열 대신 부분집합: 8! -> 2^8 x 8)
from bisect import bisect_right


def solution(n, weak, dist):
    length = len(weak)
    w = weak + [x + n for x in weak]
    k = len(dist)
    full = 1 << k
    answer = k + 1
    for start in range(length):
        # dp[mask]: mask의 친구들로 start부터 연속으로 점검 완료한 취약 지점 수
        dp = [-1] * full
        dp[0] = 0
        for mask in range(full):
            c = dp[mask]
            if c < 0:
                continue
            if c >= length:
                answer = min(answer, bin(mask).count("1"))
                continue
            pos = w[start + c]
            for f in range(k):
                if not mask & (1 << f):
                    reach = bisect_right(w, pos + dist[f], 0, start + length) - start
                    nm = mask | (1 << f)
                    if reach > dp[nm]:
                        dp[nm] = reach
    return answer if answer <= k else -1
