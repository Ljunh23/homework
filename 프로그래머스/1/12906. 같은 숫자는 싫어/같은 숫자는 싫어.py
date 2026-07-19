def solution(arr):
    answer = []
    n = len(arr)
    for i in range(n):
        if (len(answer) == 0) or answer[-1] != arr[i]:
                answer.append(arr[i])
            
        
        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer