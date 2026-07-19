def solution(x):
    answer = True
    x_arr = str(x)
    num = 0
    for i in x_arr:
        num += int(i)
    if (x % num) == 0:
        answer = True
    else:
        answer = False
    return answer