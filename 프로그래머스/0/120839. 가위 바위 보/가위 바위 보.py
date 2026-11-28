def solution(rsp):
    answer = ""
    
    win = {"0": "5","2":"0","5":"2"}
    
    for r in rsp:
        answer += win[r]
        
    return answer