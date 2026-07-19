def solution(arr):
    answer = []
    num = len(arr)
    if num == 1:
        answer = [-1]
    else:
        s = arr[0]
        s_id = arr.index(arr[0])
        for i in range(0, num):
            if s >= arr[i]:
                s = arr[i]
                s_id = arr.index(arr[i])
        del arr[s_id]
        answer = arr
    return answer