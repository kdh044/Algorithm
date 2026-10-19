# 저자 코드(길이별로 정렬한 단어 / 뒤집은 단어 리스트에서 bisect로 범위 개수 세기)와 같은 방식.
# 사용된 길이만 dict로 관리하고, 같은 키워드는 한 번만 계산하도록 다듬었다.
from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    return bisect_right(a, right_value) - bisect_left(a, left_value)


def solution(words, queries):
    array = {}
    reversed_array = {}
    for word in words:
        array.setdefault(len(word), []).append(word)
        reversed_array.setdefault(len(word), []).append(word[::-1])
    for k in array:
        array[k].sort()
        reversed_array[k].sort()

    memo = {}
    answer = []
    for q in queries:
        if q in memo:
            answer.append(memo[q])
            continue
        L = len(q)
        if L not in array:
            res = 0
        elif q[0] != '?':
            res = count_by_range(array[L], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            rq = q[::-1]
            res = count_by_range(reversed_array[L], rq.replace('?', 'a'), rq.replace('?', 'z'))
        memo[q] = res
        answer.append(res)
    return answer
