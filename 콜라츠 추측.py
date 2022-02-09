#첫번째 시도
def solution(num):
    answer = 0
    a=0
    b=0
    while num!=1:
        if num%2==0:
         num==num/2
         answer +=1
        else:
         num==num*3+1
         answer+=1
    return answer

def solution(num):
    answer = 0
    while True:
        if num==1:
            break
        elif answer==500:
            answer=-1
            break
        elif num%2==0:
            num//=2
            answer +=1
        else:
            num=num*3+1
            answer+=1
    return answer