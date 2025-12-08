n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    s = input()

    result = []
    for c in s:
        c_int = ord(c) - ord('A')          
        c_out = (a * c_int + b) % 26    
        c_char = chr(c_out + ord('A'))     
        result.append(c_char)

    print(''.join(result))
