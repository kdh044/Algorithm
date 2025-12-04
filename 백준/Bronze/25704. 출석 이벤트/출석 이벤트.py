n = int(input())
p = int(input())

candidates = [p]  
if n >= 5:
    candidates.append(p - 500)
if n >= 10:
    candidates.append(p * 90 // 100)
if n >= 15:
    candidates.append(p - 2000)
if n >= 20:
    candidates.append(p * 75 // 100)

answer = max(0, min(candidates))
print(answer)
