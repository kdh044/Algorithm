import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))
start = max(a)
end = sum(a)

while start <= end:
    mid = (start + end)//2
    mux = 0 
    count = 0
    for i in range(n):
        if  mux + a[i]> mid:
            count += 1
            mux = 0
        mux += a[i]
    if mux != 0:
        count += 1
    if count > m:
        start = mid + 1
    else:
        end = mid - 1

print(start)