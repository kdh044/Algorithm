while True:
    x , y = map(int,input().split())
    if (x and y) == 0:
        break
    if x > y:
        print("Yes")
    else:
        print("No")