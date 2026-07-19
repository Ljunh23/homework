def solution(arr, divisor):
    answer = []
    arr_len = len(arr)
    for i in range(0, arr_len):
        if (arr[i] % divisor) == 0:
            answer.append(arr[i])
    answer_len = len(answer)
    if answer_len == 0:
        answer = [-1]
    else:
        answer.sort()
    return answer