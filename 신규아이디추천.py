def solution(new_id):
    answer = ''
    #1단계 : 소문자로 치환
    new_id=new_id.lower()
    #2단계 : 소문자, 숫자, 빼기, 밑줄, 마침표만 사용
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer+=word
    #3단계 : 연속된 마침표(.) 한개로 치환 
    while '..' in answer:
        answer=answer.replace('..','.')
    #4단계 : .가 처음이나 끝에 위치하면 삭제
    if answer[0]==".":
        if len(answer)>=2:
            answer=answer[1:]
        else:
            answer="."
    if answer[-1]==".":
        answer=answer[:-1]
    #5단계
    for i in answer:
        if i==" ":
            answer.replace(i,"a")
    #6단계 : 16자리 이상인 경우 15자리까지 변경
    if len(answer)>15:
        answer=answer[:15]
        if answer[-1]=='.':
            answer=answer[:-1]
    #7단계
    if len(answer)< 3:
        answer+=answer[-1]
    return answer