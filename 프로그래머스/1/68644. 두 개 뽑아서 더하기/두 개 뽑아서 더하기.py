def solution(numbers):
    answer = []
    n = len(numbers)

    for i in range(n):
        for j in range(i+1, n):
            ans = numbers[i] + numbers[j]
            if ans not in answer:
                answer.append(ans)
    answer.sort()
    return answer