def solution(n):
    answer = 0
    i = 1
    while i*(i+1)//2 <= n:
        if i % 2 == 1 and n % i == 0: # i가 홀수 & n이 i로 나누어 떨어짐
            answer += 1
        elif i % 2 == 0 and (n/(i//2) % 2 == 1): # i가 짝수 & n을 i/2로 나눈 값이 홀수
            answer += 1
        i += 1
    return answer