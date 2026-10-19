# 저자 풀이와 같은 아이디어(작업마다 전체 구조물이 규칙을 만족하는지 검사)를
# 집합(set)으로 구현해 존재 여부 확인을 O(1)로 줄인 풀이 -> O(M^2)
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 기둥: 바닥 위 / 보의 한쪽 끝 위 / 다른 기둥 위
            if y == 0 or (x - 1, y, 1) in answer or (x, y, 1) in answer or (x, y - 1, 0) in answer:
                continue
            return False
        else:  # 보: 한쪽 끝이 기둥 위 / 양쪽 끝이 다른 보와 연결
            if (x, y - 1, 0) in answer or (x + 1, y - 1, 0) in answer or ((x - 1, y, 1) in answer and (x + 1, y, 1) in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = set()
    for x, y, stuff, operate in build_frame:
        item = (x, y, stuff)
        if operate == 0:
            answer.remove(item)
            if not possible(answer):
                answer.add(item)
        else:
            answer.add(item)
            if not possible(answer):
                answer.remove(item)
    return [list(t) for t in sorted(answer)]
