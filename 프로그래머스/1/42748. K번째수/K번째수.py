def solution(array, commands):
    answer = []
    n = len(commands)
    for a in range(n):
        num = []
        for b in range(commands[a][0]-1, commands[a][1]):
            num.append(array[b])
        num.sort()
        answer.append(num[commands[a][2]-1])
    return answer