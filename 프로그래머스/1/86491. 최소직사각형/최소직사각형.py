def solution(sizes):
    answer = 0
    l = len(sizes)
    max_w = 0
    max_h = 0
    for num in sizes:
        num.sort()
        if num[1] > max_w:
            max_w = num[1]
        if num[0] > max_h:
            max_h = num[0]
    answer = max_w * max_h
    return answer