import sys
input = sys.stdin.readline

n , m = map(int,input().split())
dna = input().strip()
a,c,t,g = map(int,input().split())

#자 이제 해야할거
#슬라이딩 윈도우는 FIFO 큐와같은 부분
#근데 그전에 문자열과 a,c,t,g의 숫자비교해서 되는지 확인하는 부분 필요함
#그걸 위해서는 a,c,t,g가 얼마나 카운팅됐는지 알려주는 함수가 필요함
#인덱스로 보내야겠다 카운팅은 함수를 만들자
#그리고 나서 슬라이딩 윈도우 알고리즘을 쓰면 되겠다.
#리스트로 먼저 만들자 빈 리스트를

A_list = [0,0,0,0]
B_list = [a,c,t,g]

def char_count(c):
    if c == 'A': return 0
    elif c == "C": return 1
    elif c == "G": return 2
    else: return 3
    
for i in range(m):
    A_list[char_count(dna[i])] += 1  #몰랐던 부분 인덱스를 하나 증가시킴

def is_True():
    for i in range(4):
        if A_list[i] < B_list[i]:
            return False
    return True

result = 1 if is_True() else 0

for i in range(m,n):
    A_list[char_count(dna[i - m])] -= 1
    A_list[char_count(dna[i])] += 1
    if is_True():
        result += 1
print(result)
    