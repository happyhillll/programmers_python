
def solution(n):
    answer = 0
    num_str=str(n)
    for i in range(len(num_str)):
        answer += int(num_str[i])
    return answer

solution(1345)


#다른 풀이
def solution(n):
    N=[int(i) for i in str(n)]
    return sum(N)