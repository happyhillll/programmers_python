def solution(arr):
    answer = 0
    hap=0
    for i in range(len(arr)):
        hap+=arr[i]
        answer=hap/len(arr)
    return answer

#ㅎㅎ...
def average(list):
    return (sum(list) / len(list))