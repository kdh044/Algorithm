def solution(key, lock):
    n = len(lock)
    m = len(key)

    pad = m - 1
    size = n + 2 * pad
    new_lock = [[0] * size for _ in range(size)]

    # 자물쇠 중앙 배치
    for i in range(n):
        for j in range(n):
            new_lock[pad + i][pad + j] = lock[i][j]

    if check(new_lock, pad, size):
        return True

    # 회전 4가지
    for _ in range(4):
        for x in range(n + pad):
            for y in range(n + pad):

                # 열쇠 겹치기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                # 자물쇠 검사
                if check(new_lock, pad, size):
                    return True

                # 원상복구
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

        key = rotate(key, m)

    return False


def check(new_lock, pad, size):
    for i in range(pad, size - pad):
        for j in range(pad, size - pad):
            if new_lock[i][j] != 1:
                return False

    return True


def rotate(key, m):
    result = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            result[j][m - i - 1] = key[i][j]

    return result
