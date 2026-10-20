def solution(n, a, operators):
    max_result = float('-inf')
    min_result = float('inf')

    def dfs(idx, result):
        nonlocal max_result, min_result

        # 모든 숫자를 사용한 경우
        if idx == n:
            max_result = max(max_result, result)
            min_result = min(min_result, result)
            return

        # 4가지 연산자 시도
        for i in range(4):
            if operators[i] > 0:
                operators[i] -= 1

                if i == 0:  # 덧셈
                    nxt = result + a[idx]
                elif i == 1:  # 뺄셈
                    nxt = result - a[idx]
                elif i == 2:  # 곱셈
                    nxt = result * a[idx]
                else:  # 나눗셈
                    nxt = abs(result) // a[idx]
                    if result < 0:
                        nxt = -nxt

                dfs(idx + 1, nxt)

                # 사용한 연산자 복구
                operators[i] += 1

    dfs(1, a[0])

    return [max_result, min_result]
