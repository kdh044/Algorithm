# 저자 코드는 O(NM) 2차원 DP. 결과는 같지만 파이썬에서 빠르게 동작하도록
# 비트 병렬 편집 거리(Myers/Hyyrö) 알고리즘으로 바꾼 정답 코드. O(N * M / w)
str1 = input().strip()
str2 = input().strip()


def edit_dist(a, b):
    m = len(a)
    peq = {}
    for i, ch in enumerate(a):
        peq[ch] = peq.get(ch, 0) | (1 << i)
    full = (1 << m) - 1
    high = 1 << (m - 1)
    pv, mv = full, 0
    score = m
    for ch in b:
        eq = peq.get(ch, 0)
        xv = eq | mv
        xh = (((eq & pv) + pv) ^ pv) | eq
        ph = mv | ~(xh | pv)
        mh = pv & xh
        if ph & high:
            score += 1
        elif mh & high:
            score -= 1
        ph = ((ph << 1) | 1) & full
        mh = (mh << 1) & full
        pv = (mh | ~(xv | ph)) & full
        mv = ph & xv
    return score


print(edit_dist(str1, str2))
