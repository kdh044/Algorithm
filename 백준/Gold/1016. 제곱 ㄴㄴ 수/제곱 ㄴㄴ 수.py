import math

low, high = map(int,input().split())
size = high - low + 1
checked = [False] * size
limit = int(math.sqrt(high))

for i in range(2, limit  + 1):
    sq = i * i
    
    start = (low // sq) * sq
    if start < low:
        start += sq
    
    for x in range(start, high + 1, sq):
        checked[x - low] = True

print(checked.count(False))