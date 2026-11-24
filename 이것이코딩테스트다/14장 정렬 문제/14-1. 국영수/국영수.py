def solution(n, students):
    students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))    
    return [x[0] for x in students]
