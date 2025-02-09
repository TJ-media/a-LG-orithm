def solution(triangle):
    n = len(triangle)
    dp = []
    for i in range(n):
        dp.append(triangle[i])
        for j in range(len(dp[i])):
            if i == 0:
                continue
            else:
                if j == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + dp[i][j]
    
    answer = max(dp[-1])
    return answer