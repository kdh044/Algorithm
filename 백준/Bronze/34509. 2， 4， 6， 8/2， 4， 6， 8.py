for n in range(10, 100):
    s = str(n)      
    tens = int(s[0])

    if tens % 4 == 0 and "8" not in s and n % 6 == 0:
        print(n)
