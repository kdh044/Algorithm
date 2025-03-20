N = int(input())
numbers = [int(input()) for i in range(N)]
numbers.sort()

for num in numbers:
    print(num)