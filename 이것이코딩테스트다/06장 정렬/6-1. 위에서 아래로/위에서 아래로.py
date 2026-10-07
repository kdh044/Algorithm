import sys
input = sys.stdin.readline

n = int(input())
answer = [int(input()) for _ in range(n)]
answer.sort(reverse = True)

print(*answer)
