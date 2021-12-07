def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    
    cnt_0=lottos.count(0)
    ans=0
    for i in win_nums:
        if i in lottos:
            ans+=1                
    return rank[cnt_0+ans],rank[ans]


#다른 방법
def solution(lottos,win_nums):
    
    rank=[6,6,5,4,3,2,1]
    count=0
    zero_count=0
    
    for num in lottos:
        if num==0:
            zero_count+=1
            continue
        
        for win_num in win_nums:
            if num == win_num:
                count+=1
    highscore=rank[zero_count+count]
    lowscore=rank[count]
    return[highscore,lowscore]
    