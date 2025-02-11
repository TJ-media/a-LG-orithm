from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 방향 및 큐 설정
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    location = deque([(0, 0, 1)])
    # 첫 번째 위치 방문처리
    maps[0][0] = 0
    
    # 큐에 남은 게 없을 때까지
    while location:
        # location의 가장 앞의 값 꺼내기
        i, j, answer = location.popleft()
        
        # 목적지에 있다면 answer 리턴
        if i == n-1 and j == m-1:
            return answer
        
        else:
            # 4가지 방향에 대해 탐색
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                
                # 주어진 n * m 칸을 벗어나지 않으며, 벽으로 막혀있지 않으면
                if 0 <= new_i < n and 0 <= new_j < m and maps[new_i][new_j] == 1:
                    # 새롭게 가는 곳 방문 처리
                    maps[new_i][new_j] = 0
                    # location에 새로운 위치 추가
                    location.append((new_i, new_j, answer+1))
                else:
                    continue
                    
    # 목적지에 도달할 수 없으면 -1 리턴
    return -1