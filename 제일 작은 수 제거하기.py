#시간초과풀이
def solution(arr):
    answer = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            while arr[i]!=arr[j]:
                if arr[i]>arr[j]:
                    answer.append(arr[i])
            if arr[i]==10:
                answer.append(-1)
    return answer

#다른 풀이
def solution(arr):
    
    if len(arr) == 1:
        arr = []
        arr.append(-1)
    else:
        arr.remove(min(arr))

    return arr