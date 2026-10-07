import sys
input = sys.stdin.readline

n = int(input())
student = [input().split() for _ in range(n)]

student.sort(key = lambda x: int(x[1]))

print(*[student[i][0] for i in range(n)])
