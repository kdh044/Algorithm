# 저자 풀이(3배 확장 + 완전 탐색)와 같은 결과를 내는 더 빠른 풀이.
# 열쇠의 돌기 좌표 집합을 회전시키며, "첫 번째 홈"을 덮는 돌기를 기준으로
# 가능한 이동량만 후보로 삼아 확인한다.
def rotate(cells, m):
    # (i, j) -> (j, m - 1 - i) : 시계 방향 90도 회전
    return [(j, m - 1 - i) for i, j in cells]


def solution(key, lock):
    n = len(lock)
    m = len(key)
    holes = set((i, j) for i in range(n) for j in range(n) if lock[i][j] == 0)
    if not holes:
        return True  # 열쇠를 자물쇠 바깥에 두면 됨
    first = min(holes)
    bumps = [(i, j) for i in range(m) for j in range(m) if key[i][j] == 1]
    if len(bumps) < len(holes):
        return False
    for _ in range(4):
        bumps = rotate(bumps, m)
        for bi, bj in bumps:
            dx, dy = first[0] - bi, first[1] - bj
            cnt = 0
            ok = True
            for i, j in bumps:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < n:
                    if lock[x][y] == 1:  # 돌기끼리 만남
                        ok = False
                        break
                    cnt += 1
            if ok and cnt == len(holes):  # 홈을 전부 채움
                return True
    return False
