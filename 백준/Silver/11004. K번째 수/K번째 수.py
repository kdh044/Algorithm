import sys
input = sys.stdin.readline

n, k = map(int,input().split())
A = list(map(int,input().split()))

A.sort()

print(A[k-1])