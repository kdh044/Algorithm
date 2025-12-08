for i in range(10,100):
    i = str(i)
    b = i[:-1]
    if int(b) % 4 == 0 and "8" not in i and int(i) % 6 == 0:
        print(int(i))