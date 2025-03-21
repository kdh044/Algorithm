count = int(input())

#각 과목 성적이 쭈루룩
#각 과목 성적에 최고점 나눠서 100곱하고 그걸 평균내라
#그렇다면 각 과목 성적을 정렬해야겠네 뭐로? sort로 
#근데 sort를 리스트만 쓸 수 있지않나? 리스트를 만들어볼까?
new_grade = []
grade = list(map(int, input().split()))
top = int(max(grade))
for i in range(count):
    tmp = grade[i] / top * 100
    new_grade.append(tmp)

answer = sum(new_grade) / count

print(answer)