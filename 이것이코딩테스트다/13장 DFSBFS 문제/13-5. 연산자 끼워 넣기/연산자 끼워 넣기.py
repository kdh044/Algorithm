import math
def solution(n, a, operators):
    max_result = (-math.inf)
    min_result = (math.inf)
    
    def dfs(idx, result):
        nonlocal max_result, min_result
        
        if idx == n:
            max_result = max(max_result,result)
            min_result = min(min_result,result)
            return
        
        for i in range(4):
            if operators[i] > 0:
                operators[i] -= 1
                if i == 0:
                    nxt = result + a[idx]
                elif i == 1:
                    nxt = result - a[idx]
                elif i == 2:
                    nxt = result * a[idx]
                else:
                    nxt = abs(result) // a[idx]
                    if result < 0:
                        nxt = -nxt
                        
                dfs(idx + 1, nxt)
                operators[i] += 1
                
    dfs(1,a[0])
    
    return (max_result,min_result)
