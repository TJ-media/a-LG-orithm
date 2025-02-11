def solution(triangle):
    n = len(triangle)
    
    # 새로운 dp 리스트 생성
    dp = []
    
    # 높이 만큼 for문 돌기(5층짜리는 다섯번)
    for i in range(n):
        # 각 층을 dp에 복사
        dp.append(triangle[i])
        
        # 각 층의 개수만큼 for문 돌기(1층은 한번, 2층은 두번)
        for j in range(len(dp[i])):
            # 1층은 스킵
            if i == 0:
                continue
            # 2층 ~ 마지막층
            else:
                # 맨 앞의 값(3층 - 8 1 0 중에 8)
                if j == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j]
                # 맨 마지막 값(3층 - 8 1 0 중에 0)
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j]
                # 가운데 값(3층 - 8 1 0 중에 1)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + dp[i][j]
    
    # 마지막 층에서 맥스 구하기
    answer = max(dp[-1])
    return answer