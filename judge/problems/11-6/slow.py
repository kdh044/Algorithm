# 한 바퀴씩(가장 작은 남은 시간만큼) 전체 목록을 다시 만드는 O(N^2) 풀이
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    rem = [(i + 1, t) for i, t in enumerate(food_times)]
    while True:
        m = min(t for _, t in rem)
        length = len(rem)
        if m * length <= k:
            k -= m * length
            rem = [(i, t - m) for i, t in rem if t > m]
        else:
            return rem[k % length][0]
