# 저자 풀이와 같은 방식이지만, stages.count(i)를 매번 호출하는 대신 한 번에 개수를 셈
def solution(N, stages):
    answer = []
    length = len(stages)

    # 각 스테이지에 머물러 있는 사람의 수
    cnt = [0] * (N + 2)
    for s in stages:
        cnt[s] += 1

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        count = cnt[i]

        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length

        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    # 정렬된 스테이지 번호 반환
    return [i[0] for i in answer]
