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

# i = 1, 2, 3, 4, 5, 6, ....

# i 홀수 
# i 짝수 
# 2 4 6 8
# 1 2 3 4

# 4 5 6 7 = 22 11
# 6 7 8 9 10 11 = 51 17