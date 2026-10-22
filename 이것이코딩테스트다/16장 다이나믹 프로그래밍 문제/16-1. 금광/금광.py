def solution(cases):
    answer = []
    
    for board in cases:
        n = len(board)
        m = len(board[0])

        gold = [[0] * m for _ in range(n)]

        for r in range(n):
            gold[r][0] = board[r][0]

        for c in range(1, m):
            for r in range(n):
                best = 0
                
                for dr in [-1,0,1]:
                    nr = r + dr
                    
                    if 0 <= nr < n:
                        best = max(best, gold[nr][c - 1])
                
                gold[r][c] = board[r][c] + best
        
        result = 0
        
        for r in range(n):
            result = max(result, (gold[r][m - 1]))
        answer.append(result)
    return answer
