# 만들 수 있는 모든 금액을 비트로 표시하는 부분합 DP: O(N * 전체 합)
n = int(input())
data = list(map(int, input().split()))
bits = 1  # 0원은 만들 수 있음
for x in data:
    bits |= bits << x
target = 1
while (bits >> target) & 1:
    target += 1
print(target)
