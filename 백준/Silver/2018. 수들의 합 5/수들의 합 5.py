import sys
input = sys.stdin.readline

n = int(input())
#투포인터로 한다했으니
#만약에 N이 15라면
#처음엔 1, 1로 시작
#12345이렇게하다가 커지면 오른쪽포인터는 가만히 왼쪽포인터는 오른쪽으로
#다시 오른쪽포인터 움직이는식으로 가야지

count = 1
start = 1
end = 1
sum1 = 1

while end != n:
    if sum1 < n:
        end += 1
        sum1 += end
    
    elif sum1 > n:
        sum1 -= start
        start += 1
    
    else:
        count += 1
        end += 1
        sum1 += end
        
print(count)