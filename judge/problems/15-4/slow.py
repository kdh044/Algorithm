# 모든 키워드마다 모든 단어와 직접 비교하는 O(단어 수 x 키워드 수) 풀이
def match(word, q):
    if len(word) != len(q):
        return False
    for a, b in zip(word, q):
        if b != '?' and a != b:
            return False
    return True

def solution(words, queries):
    return [sum(1 for w in words if match(w, q)) for q in queries]
