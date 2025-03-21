import sys
input = sys.stdin.readline

data_num,que_num = map(int,input().split())
numbers = list(map(int,input().split()))
pre_sum = [0]
temp = 0

#구간합 구하는 로직
for i in numbers:
    temp += i
    pre_sum.append(temp)
 
#합을 출력하는 로직

for j in range(que_num):
    s , e = map(int,input().split())
    print(pre_sum[e] - pre_sum[s - 1])