def solution(n, m):
    answer = []

    # 임의의 n, m 중 max, min의 값을 찾는다.
    _max, _min = max(n, m), min(n, m)
    # min의 값이 0보다 크면
    while _min:
        _max, _min = _min, _max%_min

    answer = [_max, int(n * m / _max)]
    
    return answer

#2개의 자연수 또는 정식의 최대공약수를 구하는 알고리즘
# 호제법이란 말은 두 수가 서로(互) 상대방 수를 나누어(除)서 결국 원하는 수를 얻는 알고리즘을 나타낸다.
# 2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다.