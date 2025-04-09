import sys
input = sys.stdin.readline
def solution(n, k):
    A = []
    for i in range(1,n+1):
        A.append(i)
    B = []
    for j in A:
        if j % k == 0:
            B.append(j)
    return B