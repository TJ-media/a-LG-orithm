from collections import deque
def solution(begin, target, words):
    q = deque([[begin, 0]])
    
    if target not in words:
        return 0
    
    n = len(begin)
    visited = {}
    for w in words:
        visited[w] = 0
        
    while q:
        now, cnt = q.popleft()
        if now == target:
            answer = cnt
            return answer
        
        for word in words:
            diff = 0
            for i in range(n):
                if now[i] != word[i]:
                    diff += 1
            if visited[word] == 0 and diff == 1:
                visited[word] = 1
                q.append([word, cnt+1])
                