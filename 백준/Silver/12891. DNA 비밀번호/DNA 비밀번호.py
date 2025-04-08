import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
dna = input().strip()
a, c, g, t = map(int, input().split())
checkList = [a, c, g, t]

# A, C, G, T 개수 세기 위한 리스트
def char_to_index(c):
    if c == 'A': return 0
    elif c == 'C': return 1
    elif c == 'G': return 2
    elif c == 'T': return 3

# 초기 세팅
myList = [0, 0, 0, 0]
for i in range(m):
    idx = char_to_index(dna[i])
    myList[idx] += 1

# 조건 확인 함수
def is_valid():
    for i in range(4):
        if myList[i] < checkList[i]:
            return False
    return True

# 초기 윈도우 검사
result = 1 if is_valid() else 0

# 윈도우 이동하며 검사
for i in range(m, n):
    out_char = dna[i - m]
    in_char = dna[i]
    myList[char_to_index(out_char)] -= 1
    myList[char_to_index(in_char)] += 1
    if is_valid():
        result += 1

print(result)
