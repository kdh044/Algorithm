def solution(n, houses):

    houses.sort()
    
    return houses[(n - 1) // 2]
