# 숫자 -> 영어

def solution(s):
    if s==0 or s=="zero":
        print("결과없음")
    alphabet={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    answer=0
    for i in s:
        if i.isnumeirc() == True:
            i.replace(i,alphabet[i])
            answer+=i
        else: 
            answer+=i
    return answer

# 영어 -> 숫자

def solution(s):
    if s[0]==0 or s[0]=="zero":
        print("결과없음")
    dic={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    answer=''
    corpus=''
    a=''
    for i in s:
        if i.isdigit():
            answer=answer+i
        else:
            corpus=corpus+i
            if corpus in dic.keys():
                answer+=str(dic[corpus])
                corpus=''
    return int(answer)
    
#다른 답

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)