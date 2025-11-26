from queue import PriorityQueue
n = int(input())
pq = PriorityQueue()

for _ in range(n):
    date = int(input())
    pq.put(date)

data1 = 0
data2 = 0
answer = 0

while pq.qsize() > 1:
    data1 = pq.get()
    data2 = pq.get()
    temp = data1 + data2
    answer += temp
    pq.put(temp)

print(answer)