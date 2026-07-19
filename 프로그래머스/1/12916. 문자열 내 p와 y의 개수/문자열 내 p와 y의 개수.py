def solution(s):
    answer = True
    cnt_p = 0
    cnt_y = 0
    s = s.lower()
    for char in s:
        if char == 'p':
            cnt_p += 1
        elif char == 'y':
            cnt_y += 1

    if cnt_p == cnt_y:
        answer = True
    else:
        answer = False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer