# 첫번쨰 시도
def solution(phone_number):
    answer = ''
    a=list(phone_number)
    for i in range(a[:-4]):
        i.replace("*")
        answer.append(i)
    return answer

#두번째 시도
def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)):
        for j in range (len(phone_number[:-4])):
            phone_number[j]="*"
            answer+=phone_number[j]
    answer+=phone_number[i]
    return answer #실패

#답
def solution(phone_number):
    num = len(phone_number)
    back = phone_number[-4:]
    return "*"*(num-4)+back

def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]