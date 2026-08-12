def solution(myStr):
    for s in "abc":
        myStr = myStr.replace(s," ")
    
    answer = myStr.split()
    return answer if answer else ["EMPTY"]