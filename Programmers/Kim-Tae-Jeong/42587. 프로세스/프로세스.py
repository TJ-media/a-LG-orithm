def solution(priorities, location):
    # priorities를 정렬한 새로운 리스트 생성
    sorted_arr = sorted(priorities, reverse = True)
    
    idx = 0
    n = len(priorities)
    answer = 0
    # priorities를 돌면서 우선순위가 큰 순서대로 찾음
    for i in range(n):
        while priorities[idx] != sorted_arr[i]:
            # idx를 1 증가시킴
            if idx < n - 1: 
                idx += 1
            # 맨 마지막인 경우 idx를 다시 0으로(맨 앞으로)
            else:
                idx = 0
        # 찾으면 우선순위 탐색 안되도록 0으로 수정
        priorities[idx] = 0
        
        if idx != location:
            continue
        # location번째 우선순위를 가진 값 리턴
        else:
            answer = i + 1
            break
    return answer