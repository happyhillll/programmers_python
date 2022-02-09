def solution(n):
    a=list(str(n))
    answer=a.reverse()
    return answer

def solution(n):
    a=str(n)
    a.reverse()
    answer=list(a)
    return answer

def solution(n):
    b=list(reversed(n))
    return b

#정답
def solution(n):
    a = list(str(n))
    a.reverse()
    
    return list(map(int, a))

#map는 리스트의 요소를 함수로 처리해주는 함수