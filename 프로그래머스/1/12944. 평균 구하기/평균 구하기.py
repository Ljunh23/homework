def solution(arr):
    answer = 0
    n = len(arr)
    for i in arr:
        answer += i
    answer = answer/n
    return answer