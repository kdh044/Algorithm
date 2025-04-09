

n = int(input())
a = list(map(int,input().split()))

#탐색으로 가면 n^2이라 안되고 역시 n번반복한다음 스택으로 찾아야겠지
#일단은 반복문으로 리스트의 요소들을 꺼내
#그리고 그 다음수들을 한개 넣어
#여기서 if문으로 분기
#만약 오른쪽의 수가 지금 수보다 크다 
#pop으로 뽑고 끝
#근데 오른쪽의 수가 지금보다 작아?
#그럼 무시하고 다음수 또 넣어
#끝까지 갔는데 나보다 큰수가없네? -1출력
#이걸 n반복으로 하면 완전탐색이니까 while반복문써서 탐색으로 가자
result = [-1] * n
stack = []

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        index = stack.pop()
        result[index] = a[i]
    stack.append(i)

print(" ".join(map(str,result)))