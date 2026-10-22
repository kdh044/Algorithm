def solution(n, students):
    students.sort(key = lambda x: x[1])
    return [student[0] for student in students]
