import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
A = list(map(int,input().split()))

#리스트로 받았다 이거지 
#이거 투포인터로 풀면 되네
#근데 그중에서 두개의 수만 고르면될텐데, 순열 알고리즘이있나?
#그전에 정렬부터하자
A.sort()

#그 다음에 첫번째 포인터와 두번째 포인터 정렬
start = 0
end = n - 1
sum1 = 0
count = 0

while start < end :
    #여기가 문제네 
    #포인터가 안겹쳐야하고 두가지 수를 잡아야함 어떻게하지
    if A[start] + A[end] < m:
        start += 1
    elif A[start] + A[end] > m:
        end -= 1
    else:
        count += 1
        start += 1
        end -= 1
    
        
print(count)
        