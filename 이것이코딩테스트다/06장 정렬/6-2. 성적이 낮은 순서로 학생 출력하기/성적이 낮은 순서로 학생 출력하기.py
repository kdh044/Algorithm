import sys
input = sys.stdin.readline

n = int(input())
student = [input().split() for _ in range(n)]

student.sort(key = lambda x: int(x[1]))

print(*[x[0] for x in student])
