def solution(n):
    answer = []
    num = str(n)
    num_len = len(num)
    for i in num:
        answer.append(int(i))
    answer.reverse()
        
    return answer