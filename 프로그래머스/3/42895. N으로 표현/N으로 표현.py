def solution(N, number):
    answer = 0
    dp = [[] for _ in range(9)]
    
    # dp1과 2만 직접 설정
    dp[1] = [N]
    dp[2] = [N*11, N+N, N-N, N*N, int(N/N)]
    if number == N:
        return 1
    elif number in dp[2]:
        return 2
    
    for i in range(3, 9):
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].append(a+b)
                    dp[i].append(a-b)
                    dp[i].append(a*b)
                    dp[i].append(int(a/b) if b != 0 else 0)
        dp[i].append(int(str(N)*i))
        if number in dp[i]:
            return i
    # 3 = 12 21 3
    # 4 = 13 22 31 4
    # 5 = 14 23 32 41 5
    # 6 = 15 24 33 42 51 6
    # 7 = 16 25 34 43 52 61 7
    # 8 = 17 26 35 44 53 62 71 8
    
    return -1