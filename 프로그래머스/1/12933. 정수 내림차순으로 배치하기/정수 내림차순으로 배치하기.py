def solution(n):
    answer = ""
    num = str(n)
    num_arr = []
    for i in num:
        num_arr.append(i)
    num_arr.sort()
    num_arr.reverse()
    for j in num_arr:
        answer += j
    return int(answer)