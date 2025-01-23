def solution(n, lost, reserve):
    # 도난 당한 사람 중 여벌옷 있는 사람 제거
    reserve, lost = list(set(reserve) - set(lost)), list(set(lost) - set(reserve))
    lost.sort()
    reserve.sort()
    
    print(lost)
    print(reserve)
    print("------------------")
    
    # 앞뒤 사람 탐색
    for j in reserve:
        if j - 1 in lost:
            lost.remove(j - 1)
            print(lost)
            print(reserve)
        else:
            if j + 1 in lost:
                lost.remove(j + 1)
                print(lost)
                print(reserve)
            else:
                continue
    answer = n - len(lost)
    return answer