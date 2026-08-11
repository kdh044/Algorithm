def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)

    def dfs(fatigue, count):
        nonlocal answer
        answer = max(answer, count)

        for i in range(len(dungeons)):
            required, cost = dungeons[i]

            if not visited[i] and fatigue >= required:
                visited[i] = True
                dfs(fatigue - cost, count + 1)
                visited[i] = False

    dfs(k, 0)
    return answer