def solution(progresses, speeds):
    answer = []
    while progresses:
        a = 0
        while a < len(progresses) and progresses[a] >= 100:
            a += 1
            
        if a != 0:
            answer.append(a)
            for _ in range(a):
                progresses.pop(0)
                speeds.pop(0)
            
        for i in range(len(speeds)):
            progresses[i] += speeds[i]

    return answer