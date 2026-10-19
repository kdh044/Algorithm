# 저자 풀이(재귀 DFS, ref_author.py)는 1000x1000에서 재귀 한도를 넘으므로
# 같은 결과(연결 요소 개수)를 내는 빠른 스캔라인 flood fill 버전
import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    W = m + 1
    g = bytearray(b'1' * (W * (n + 2) + 1))
    for i in range(n):
        g[(i + 1) * W:(i + 1) * W + m] = data[2 + i]
    find = g.find
    rfind = g.rfind
    ONES = b'1' * W
    cnt = 0
    end = W * (n + 1)
    s = find(b'0', W, end)
    while s != -1:
        cnt += 1
        if g[s + 1] == 49 and g[s + W] == 49:
            g[s] = 49
            s = find(b'0', s, end)
            continue
        st = [s]
        pop = st.pop
        push = st.append
        while st:
            v = pop()
            if g[v] != 48:
                continue
            if g[v - 1] == 49 and g[v + 1] == 49:
                g[v] = 49
                if g[v - W] == 48:
                    push(v - W)
                if g[v + W] == 48:
                    push(v + W)
                continue
            l = rfind(b'1', 0, v) + 1
            r = find(b'1', v)
            g[l:r] = ONES[:r - l]
            for a, b in ((l - W, r - W), (l + W, r + W)):
                k = find(b'0', a, b)
                while k != -1:
                    push(k)
                    k = find(b'1', k, b)
                    if k == -1:
                        break
                    k = find(b'0', k, b)
        s = find(b'0', s, end)
    print(cnt)


main()
