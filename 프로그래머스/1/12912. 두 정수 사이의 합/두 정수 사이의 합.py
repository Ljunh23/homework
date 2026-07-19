def solution(a, b):
    answer = 0
    big_num = 0
    small_num = 0
    if a < b:
        big_num = b
        small_num = a
    else:
        big_num = a
        small_num = b
    for i in range(small_num, big_num + 1):
        answer += i
    return answer