import sys
input = sys.stdin.readline

n = int(input())

students = [input().split() for _ in range(n)]
students.sort(key=lambda x: int(x[1]))

print(*[student[0] for student in students])
