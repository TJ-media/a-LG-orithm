from collections import deque
def solution(queue1, queue2):
    # popleft()가 pop(0)보다 빨라서 deque 사용
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    # half 구하기
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    half = (sum1 + sum2) // 2

    answer = 0
    # 큐 2개에서 나올 수 있는 작업 최댓값은 얼마일까?
    length = int((len(queue1) + len(queue2)) * 1.5)
    for _ in range(length):
        # sum1이 half보다 작으면
        # queue2에서 pop해서 queue1에 append 해줌 
        if sum1 < half:
            a = queue2.popleft()
            sum1 += a
            queue1.append(a)
            answer += 1
        # sum1이 half보다 크면
        # queue1에서 pop해서 queue2에 append 해줌
        elif sum1 > half:
            b = queue1.popleft()
            sum1 -= b
            queue2.append(b)
            answer += 1
        # 같으면 answer 리턴
        else:
            return answer
    # 다 돌아도 안되면 -1 리턴
    return -1