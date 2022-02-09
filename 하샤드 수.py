def solution(x):
    a=list(str(x))
    sum=0
    for i in range(len(a)):
        sum += int(a[i])
        if x%sum==0:
            answer=True
        else:
            answer=False
    return answer
