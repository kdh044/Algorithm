import sys
input = sys.stdin.readline

n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1  # 다음에 push할 수

for target in sequence:
    while current <= target:
        stack.append(current)
        result.append('+')
        current += 1

    # 현재 target이 스택 맨 위에 있어야 pop 가능
    if stack and stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        sys.exit(0)

# 정상적으로 종료되었을 경우 출력
for r in result:
    print(r)
