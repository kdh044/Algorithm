import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
A.sort()

#정렬까지 끝

#일단 단순하게 생각해보자
#완전탐색쓰면 쉽긴하지만 거의 모든경우 에러가 난다. 시간초과오류
#그러니까 투포인터를 써야겠지
#근데 여기는 m이 따로 안주어졌네? 어떻게풀어야지...
#일단 얼마나 반복해야 할지 모르겠으니까 while문으로 가보자
#시작 인덱스와 마지막 인덱스도 만들어야겠다
result = 0

for k in range(n):  
    find = A[k]
    i = 0
    j = n - 1
    while i < j:
        if i == k:
            i += 1
            continue
        if j == k:
            j -= 1
            continue
        if A[i] + A[j] == A[k]:
            result += 1
            break
        elif A[i] + A[j] < A[k]:
            i += 1
        elif A[i] + A[j] > A[k]:
            j -= 1

            
print(result)