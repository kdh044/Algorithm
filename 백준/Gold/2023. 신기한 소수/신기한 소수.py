import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())

def isPrime(num):
    if num == 2:
        return True
    elif num % 2 == 0 or num < 2:
        return False
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
                
            a = 10 * number + i
            if isPrime(a):
                DFS(a)
DFS(2)
DFS(3)
DFS(5)
DFS(7)