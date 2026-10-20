def solution(s):
    result = []
    total = 0

    for x in s:
        if x.isalpha():
            result.append(x)
        else:
            total += int(x)

    result.sort()

    if total != 0:
        result.append(str(total))

    return "".join(result)
