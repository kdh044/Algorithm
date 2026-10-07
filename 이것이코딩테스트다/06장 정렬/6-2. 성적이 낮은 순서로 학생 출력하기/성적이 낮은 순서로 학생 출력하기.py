import sys
input = sys.stdin.readline

n = int(input())

grade = {
    name: int(num)
    for name, num in (input().split() for _ in range(n))
}

print(*sorted(grade, key=grade.get))
