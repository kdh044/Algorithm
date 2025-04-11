def solution(arr, intervals):
    a,b = intervals[0], intervals[1]
    c = arr[a[0]:a[-1] + 1]
    d = arr[b[0]:b[-1] + 1]
    answer = c + d
    return answer