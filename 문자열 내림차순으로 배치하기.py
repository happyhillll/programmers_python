def solution(s):
    return(''.join(sorted(s,reverse=True)))
        
#다른 풀이
def solution(s):
    answer=''
    list=sorted(s,reverse=True)
    
    for i in list:
        answer += i
    return answer