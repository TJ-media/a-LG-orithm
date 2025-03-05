from collections import deque
def solution(n, edge):
    
    # 딕셔너리에 그래프 빈 배열 할당
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    # 그래프 그리기
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # 각 노드 방문 기록 초기화(1 ~ n+1)
    visited = [-1] * (n+1)
    visited[1] = 0
    
    # BFS
    q = deque([1])
    while q:
        current = q.popleft()
        for neighbor in graph[current]:
            if visited[neighbor] == -1:                    # 방문하지 않은 노드라면
                visited[neighbor] = visited[current] + 1   # 1로부터 거리 기록
                q.append(neighbor)                         # q에 탐색해야할 노드 추가
            else:
                continue
        
    # 최댓값 개수 구하기
    max_dist = max(visited)
    answer = 0
    for k in visited:
        if k == max_dist:
            answer += 1
        else:
            continue
    return answer