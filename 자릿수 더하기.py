
def solution(n):
    answer = 0
    num_str=str(n)
    for i in range(len(num_str)):
        answer += int(num_str[i])
    return answer

solution(1345)
