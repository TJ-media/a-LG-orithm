def solution(N, stages):
    stages.sort()
    
    result = [[i, 0] for i in range(1, N+1)]
    # print(result)
    total = len(stages)
    
    for i in range(1, N+1):
        cnt = stages.count(i)
        result[i-1][1] = cnt / total if total > 0 else 0
        total -= cnt
        
    result.sort(key=lambda x:x[1], reverse = True)
    answer = [x[0] for x in result]
    return answer