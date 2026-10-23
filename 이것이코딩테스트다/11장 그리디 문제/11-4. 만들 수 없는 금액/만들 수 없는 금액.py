def solution(n, coins):
    target = 1
    coins.sort()
    
    for coin in coins:
        if coin > target:
            break
            
        target += coin
        
    return target
