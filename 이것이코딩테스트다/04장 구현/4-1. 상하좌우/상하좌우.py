import sys
input = sys.stdin.readline

R = [0,1]
D = [1,0]
L = [0,-1]
U = [-1,0]

n = int(input())
direction = list(map(str,input().split()))

position = [1,1]

for direct in direction:
    if direct == 'R':
        move = R
    elif direct == 'D':
        move = D
    elif direct == 'L':
        move = L
    else:
        move = U

    next_position = [
        position[0] + move[0],position[1] + move[1]
    ]
    if 1 <= next_position[0] <= n and 1 <= next_position[1] <= n:
        position = next_position

print(*position)
