import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())

def isPrime(num):
    # 2는 소수입니다
    if num == 2:
        return True
    # 1과 짝수는 소수가 아닙니다 (2 제외)
    if num < 2 or num % 2 == 0:
        return False
    # 제곱근까지만 체크하면 됩니다
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def DFS(number):
    if len(str(number)) == n:
        print(number)
    else:
        for i in range(1,10):
            if i % 2 == 0:
                continue
            if isPrime(number * 10 + i):
                DFS(number * 10 + i)
DFS(2)
DFS(3)
DFS(5)
DFS(7)
