n = int(input())
before = input()
after = input()

inverted = ''.join("1" if c == "0" else "0" for c in before)

if n % 2 == 0:
    x = before
else:
    x = inverted

if (x == after):
    print("Deletion succeeded")
else:
    print("Deletion failed")