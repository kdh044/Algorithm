import sys
input = sys.stdin.readline

dx = [2,2,-2,-2,1,-1,1,-1]
dy = [1,-1,1,-1,2,2,-2,-2]

n = input()

row = int(n[1])
col = int(ord(n[0]) - ord("a") + 1)

count = 0

for i in range(8):
    x = row + dx[i]
    y = col + dy[i]
    
    if 1 <= x <= 8 and 1 <= y <= 8:
        count += 1
        
print(count)
