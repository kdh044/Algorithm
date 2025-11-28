l = int(input())
r = int(input())

total = 0
level = 1
while(True):
    l = (l * r // 100)
    if l <= 5:
        break
    total += (2 ** level) * l
    level += 1

print(total)