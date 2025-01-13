import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    if scoville[0] >= K:
        return 0
    while len(scoville) > 1:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville) * 2
        
        heapq.heappush(scoville, a + b)
        answer += 1
        
        if scoville[0] >= K:
            return answer
        
    if scoville[0] >= K:
        return answer
    else:
        return -1