def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)

    both = lost & reserve
    lost -= both
    reserve -= both

    borrowed = 0

    for student in sorted(lost):
        if student - 1 in reserve:
            reserve.remove(student - 1)
            borrowed += 1
        elif student + 1 in reserve:
            reserve.remove(student + 1)
            borrowed += 1

    return n - len(lost) + borrowed