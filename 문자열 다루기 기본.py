def solution(s):
    if len(s)==4 or len(s)==6:
        if s.isdigit():
            return True
        else:
            return False
    else:
        return False
    
#다른 풀이
def solution(s):
    return s.isdigit() and len(s) in (4,6)