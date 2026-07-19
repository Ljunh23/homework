def solution(a, b, n):
    total = (n//a)*b
    answer = total
    emp = total + (n % a)
    while emp >= a:
        total = (emp//a)*b
        emp = total + (emp % a)
        answer += total
    return answer