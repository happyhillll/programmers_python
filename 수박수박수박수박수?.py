def solution(n):
    answer = ''
    a=''
    b=''
    c=''
    for i in range(n):
        if i%2==0:
            a="수"
            answer+=str(a)
        elif i==0:
            b="수"
            answer+=str(b)
        else:
            c="박"
            answer+=str(c)
    return answer

#다른 사람 풀이
def solution(n): 
    return ('수박'*n) [:n]
# []: 슬라이싱