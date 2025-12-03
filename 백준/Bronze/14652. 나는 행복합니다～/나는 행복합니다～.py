import sys
input = sys.stdin.readline

x , y , z= map(int,input().split())

a = z // y
b = z % y

print(a, b)