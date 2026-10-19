# 저자 풀이(우선순위 큐)와 같은 아이디어를, 힙 대신 한 번의 정렬로 처리해 상수를 줄인 코드
def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 (음식 시간, 음식 번호) 순으로 정렬
    order = sorted(range(len(food_times)), key=food_times.__getitem__)

    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    length = len(food_times)  # 남은 음식의 개수
    pos = 0
    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + (food_times[order[pos]] - previous) * length <= k:
        now = food_times[order[pos]]
        sum_value += (now - previous) * length
        length -= 1  # 다 먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정
        pos += 1

    # 남은 음식 중에서 몇 번째 음식인지 확인 (음식 번호 기준 정렬)
    remain = sorted(order[pos:])
    return remain[(k - sum_value) % length] + 1
