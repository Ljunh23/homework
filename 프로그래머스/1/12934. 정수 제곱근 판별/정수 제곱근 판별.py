def solution(n):
    answer = 0
    sqrt = n ** (1/2)
    num = int(sqrt)
    if sqrt == num:
        answer = (num+1)**2
    else:
        answer = -1

            
    return answer