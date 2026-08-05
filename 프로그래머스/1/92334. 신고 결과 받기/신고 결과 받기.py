def solution(id_list, report, k):
    report = set(report)
    reported_count = {}
    mail_count = {}
    
    for user in id_list:
        reported_count[user] = 0
        mail_count[user] = 0
        
    for data in report:
        reporter, reported = data.split()
        reported_count[reported] += 1
        
    for data in report:
        reporter, reported = data.split()
        
        if reported_count[reported] >= k:
            mail_count[reporter] += 1
    
    answer = []
    for user in id_list:
        answer.append(mail_count[user])
    
    return answer