def solution(s, n):
    a='abcedfghijklmnopqrstuvwxyz'
    A='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    for i in s:
        if i in a:
            answer += a[(a.index(i)+n)%26]
        elif i in A:
            answer += A[(A.index(i)+n)%26]
        else:
            answer += " "
    return answer