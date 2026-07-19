def solution(phone_number):
    answer = ''
    n = len(phone_number)
    print(n)
    num = []
    for j in phone_number:
        num.append(int(j))
    for i in range(0, n):
        if (n -1 -i) >= 4:
            answer += '*'
        else:
            answer += str(num[i])
    return answer