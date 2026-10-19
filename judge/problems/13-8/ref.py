# 저자 풀이와 같은 BFS. 방문 처리를 리스트 대신 배열로 해서 O(N^2)으로 동작하도록 바꾼 버전.
# 칸 번호 p(외곽에 벽을 두른 좌표) 하나로 위치를 표현한다.
#   가로 상태: p, p+1 두 칸 / 세로 상태: p, p+W 두 칸
def solution(board):
    n = len(board)
    W = n + 2
    b = [1] * (W * W)
    for i in range(n):
        b[(i + 1) * W + 1:(i + 1) * W + 1 + n] = board[i]
    goal = n * W + n
    seen_h = [False] * (W * W)  # 가로 상태 방문 여부
    seen_v = [False] * (W * W)  # 세로 상태 방문 여부
    start = W + 1
    seen_h[start] = True
    cur_h, cur_v = [start], []
    cost = 0
    while cur_h or cur_v:
        nh, nv = [], []
        for p in cur_h:
            if p == goal or p + 1 == goal:
                return cost
            # 평행 이동
            for np_ in (p + 1, p - 1, p + W, p - W):
                if not seen_h[np_] and b[np_] == 0 and b[np_ + 1] == 0:
                    seen_h[np_] = True
                    nh.append(np_)
            # 위/아래로 회전
            u = p - W
            if b[u] == 0 and b[u + 1] == 0:
                if not seen_v[u]:
                    seen_v[u] = True; nv.append(u)
                if not seen_v[u + 1]:
                    seen_v[u + 1] = True; nv.append(u + 1)
            d = p + W
            if b[d] == 0 and b[d + 1] == 0:
                if not seen_v[p]:
                    seen_v[p] = True; nv.append(p)
                if not seen_v[p + 1]:
                    seen_v[p + 1] = True; nv.append(p + 1)
        for p in cur_v:
            if p == goal or p + W == goal:
                return cost
            for np_ in (p + 1, p - 1, p + W, p - W):
                if not seen_v[np_] and b[np_] == 0 and b[np_ + W] == 0:
                    seen_v[np_] = True
                    nv.append(np_)
            # 왼쪽/오른쪽으로 회전
            l = p - 1
            if b[l] == 0 and b[l + W] == 0:
                if not seen_h[l]:
                    seen_h[l] = True; nh.append(l)
                if not seen_h[l + W]:
                    seen_h[l + W] = True; nh.append(l + W)
            r = p + 1
            if b[r] == 0 and b[r + W] == 0:
                if not seen_h[p]:
                    seen_h[p] = True; nh.append(p)
                if not seen_h[p + W]:
                    seen_h[p + W] = True; nh.append(p + W)
        cur_h, cur_v = nh, nv
        cost += 1
    return 0
