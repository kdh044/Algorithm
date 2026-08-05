def solution(id_list, report, k):
    # 같은 사람이 같은 사람을 여러 번 신고한 경우 제거
    report = set(report)

    # 각 사용자가 신고당한 횟수
    reported_count = {}

    # 각 사용자가 받을 메일 수
    mail_count = {}

    for user in id_list:
        reported_count[user] = 0
        mail_count[user] = 0

    # 각 사용자가 신고당한 횟수 계산
    for data in report:
        reporter, reported = data.split()

        reported_count[reported] += 1

    # 신고당한 사람이 정지되었다면 신고자에게 메일 추가
    for data in report:
        reporter, reported = data.split()

        if reported_count[reported] >= k:
            mail_count[reporter] += 1

    # id_list 순서대로 메일 수 반환
    answer = []

    for user in id_list:
        answer.append(mail_count[user])

    return answer