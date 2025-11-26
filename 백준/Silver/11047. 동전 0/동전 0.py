n, k = map(int,input().split())
a = [0] * n;
coin = 0

for j in range(n):
    a[j] = int(input())
    
for i in range(n - 1, -1, -1):
    if (a[i]) <= k:
        coin += k // a[i]
        k = k % a[i]

print(coin)
        