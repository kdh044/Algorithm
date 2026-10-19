# 삽입 정렬로 직접 정렬하는 O(N^2) 풀이
n = int(input())
students = []
for _ in range(n):
    a = input().split()
    students.append(((-int(a[1]), int(a[2]), -int(a[3]), a[0]), a[0]))
for i in range(1, n):
    j = i
    while j > 0 and students[j - 1][0] > students[j][0]:
        students[j - 1], students[j] = students[j], students[j - 1]
        j -= 1
for _, nm in students:
    print(nm)
