# 저자 답안 7-6(계수 정렬) 방식을 빠른 입력으로 변형한 버전
import sys

data = sys.stdin.buffer.read().split()
n = int(data[0])
# 가게에 있는 전체 부품 번호를 기록 (번호는 100만 이하)
array = bytearray(1000001)
for i in data[1:n + 1]:
    array[int(i)] = 1
m = int(data[n + 1])
# 손님이 확인 요청한 부품 번호를 하나씩 확인
print(' '.join(['yes' if array[int(i)] else 'no' for i in data[n + 2:n + 2 + m]]))
