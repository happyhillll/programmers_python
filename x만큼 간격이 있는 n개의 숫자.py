def solution(x, n):
    answer = []
    while True:
        for i in range(n):
            a=x+(i*x)
            answer.append(a)
        return answer