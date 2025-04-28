import sys


A = list(input().strip())

for i in range(len(A)):
    Max = i
    for j in range(i+1, len(A)):
        if A[Max] < A[j]:
            Max = j
    
    if A[i] < A[Max]:
        temp = A[i]
        A[i] = A[Max]
        A[Max] = temp
        
print(''.join(A))