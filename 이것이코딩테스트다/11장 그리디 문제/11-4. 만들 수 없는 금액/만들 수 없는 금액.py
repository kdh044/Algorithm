def solution(n, coins):
    coins.sort()
    target = 1
    
    for coin in coins:
        if coin > target:
            break
            
        target += coin
      
    return target
