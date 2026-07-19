def solution(x, n):
    answer = []
    if x == 0:
        answer = [0] * n
    else:
        for i in range(1, n+1):
            answer.append(i * x)            
    
    return answer