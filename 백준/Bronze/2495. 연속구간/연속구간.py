for _ in range(3):
    x = input()
    cnt = 1        
    ans = 1      
    for i in range(1, len(x)):
        if x[i] == x[i - 1]:
            cnt += 1
        else:
            cnt = 1
        if cnt > ans:
            ans = cnt
    print(ans)
            
    