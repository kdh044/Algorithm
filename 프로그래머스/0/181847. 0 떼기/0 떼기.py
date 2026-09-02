def solution(n_str):
    count = 0
    for n in n_str:
        if n != "0":
            break
        count += 1
    return n_str[count:]