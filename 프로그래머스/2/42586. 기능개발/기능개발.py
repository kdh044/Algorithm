def solution(progresses, speeds):
    days = []

    for progress, speed in zip(progresses, speeds):
        day = (100 - progress + speed - 1) // speed
        days.append(day)

    answer = []
    current = days[0]
    count = 1

    for day in days[1:]:
        if day <= current:
            count += 1
        else:
            answer.append(count)
            current = day
            count = 1

    answer.append(count)

    return answer