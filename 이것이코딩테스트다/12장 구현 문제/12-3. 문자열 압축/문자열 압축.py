def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[:step]
        count = 1

        for i in range(step, len(s), step):
            current = s[i:i + step]

            if current == prev:
                count += 1
            else:
                if count > 1:
                    compressed += str(count)

                compressed += prev
                prev = current
                count = 1

        if count > 1:
            compressed += str(count)

        compressed += prev

        answer = min(answer, len(compressed))

    return answer
