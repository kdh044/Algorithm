def solution(n, consultations):
    answer = 0

    def dfs(day, money):
        nonlocal answer

        if day >= n:
            answer = max(answer, money)
            return

        t, p = consultations[day]

        # 오늘 상담을 하지 않는 경우
        dfs(day + 1, money)

        # 오늘 상담을 하는 경우
        if day + t <= n:
            dfs(day + t, money + p)

    dfs(0, 0)
    return answer
