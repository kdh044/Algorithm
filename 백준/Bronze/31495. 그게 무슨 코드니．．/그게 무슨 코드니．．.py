n = input()

if len(n) >= 2 and  n[-1] == "\"" and n[0] == "\"" :
    inner = n[1:-1]
    if inner.strip() != "":
        print(inner)
    else:
        print("CE")
else:
    print("CE")