import sys
input = sys.stdin.readline

n = int(input())
students = []

for _ in range(n):
    name,kor,eng,math = input().split()
    students.append([name, int(kor), int(eng), int(math)])
    
students.sort(key=lambda x: (-x[1],x[2],-x[3],x[0]))
print('\n'.join([x[0] for x in students]))