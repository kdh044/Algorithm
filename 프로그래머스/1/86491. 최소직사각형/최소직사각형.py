def solution(sizes):
    max_h = 0
    max_w = 0
    for h,w in sizes:
        if h > w:
            w, h = h, w
        max_w = max(max_w,w)
        max_h = max(max_h,h)
    answer = max_w * max_h
    return answer