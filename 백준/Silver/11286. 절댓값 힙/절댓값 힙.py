import sys
from queue import PriorityQueue

input = sys.stdin.readline
N = int(input())

myQueue = PriorityQueue()

for _ in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print(0)
        else:
            temp = myQueue.get()
            print(temp[1])
    else:
        myQueue.put((abs(request), request))  # 절댓값 기준 정렬, tie-break는 원래 값
