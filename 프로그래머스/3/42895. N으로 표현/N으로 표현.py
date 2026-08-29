def solution(N, number):
    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        # N을 i번 이어 붙인 숫자
        dp[i].add(int(str(N) * i))

        # i = j + (i-j)로 나누어 이전 결과를 조합
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)

                    if b != 0:
                        dp[i].add(a // b)

        # i번 사용해서 number를 만들 수 있다면
        if number in dp[i]:
            return i

    return -1