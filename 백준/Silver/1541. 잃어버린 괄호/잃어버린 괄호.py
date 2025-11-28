a = input().split("-")
total = 0

total = sum(map(int,a[0].split("+")))

for p in a[1:]:
    total -= sum(map(int, p.split('+')))

print(total)

