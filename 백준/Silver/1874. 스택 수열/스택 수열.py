import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
num = 1
answer = []
stack = []
for i in range(n):
    if a[i] >= num:
        while a[i] >= num:
            stack.append(num)
            num += 1
            answer.append("+")
        stack.pop()
        answer.append("-")
    else:
        if stack[-1] != a[i]:
            print("NO")
            sys.exit(0)
        answer.append("-")
        stack.pop()
print('\n'.join(answer))