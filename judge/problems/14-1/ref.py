# 저자 풀이(14-1)와 같은 정렬 기준. PyPy에서는 튜플 키 정렬이 느려서
# 1) 이름으로 먼저 정렬한 뒤 2) 점수 세 개를 정수 하나로 묶은 키로 안정 정렬한다(결과는 같음).
import sys

data = sys.stdin.buffer.read().split()
n = int(data[0])
names = data[1:4 * n + 1:4]
kor = data[2:4 * n + 2:4]
eng = data[3:4 * n + 3:4]
mat = data[4:4 * n + 4:4]
order = sorted(range(n), key=names.__getitem__)
score = [(100 - int(kor[i])) * 1000000 + int(eng[i]) * 1000 + (100 - int(mat[i])) for i in range(n)]
order.sort(key=score.__getitem__)
sys.stdout.buffer.write(b"\n".join([names[i] for i in order]) + b"\n")
