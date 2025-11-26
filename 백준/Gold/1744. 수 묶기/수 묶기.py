from queue import PriorityQueue
pluspq = PriorityQueue()
minuspq = PriorityQueue()
one = 0
zero = 0
n = int(input())

for _ in range(n):
    data = int(input())
    if data > 1:
        pluspq.put(data * -1)
    elif data == 1:
        one += 1
    elif data == 0:
        zero += 1
    else:
        minuspq.put(data)
        
answer = 0

while pluspq.qsize() > 1:
    first = pluspq.get() * -1
    second = pluspq.get() * -1
    answer += first * second

if pluspq.qsize() > 0:
    answer += pluspq.get() * -1

while minuspq.qsize() > 1:
    first = minuspq.get()
    second = minuspq.get()
    answer += first * second

if minuspq.qsize() > 0:
    if zero == 0:
        answer += minuspq.get()
        
answer += one

print(answer)