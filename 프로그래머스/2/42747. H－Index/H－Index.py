def solution(citations):
    # 내림차순으로 정렬
    citations.sort(reverse=True)
    
    # 인용된 논문 개수 idx
    idx = 0
    # 전체 논문 돌면서
    for i in citations:
        # 인용 횟수, 인용된 논문 개수 비교
        # [6, 5, 3, 1, 0]
        #  0, 1, 2, 3, 4
        if i >= idx + 1:
            idx += 1
        else:
            break
            
    return idx