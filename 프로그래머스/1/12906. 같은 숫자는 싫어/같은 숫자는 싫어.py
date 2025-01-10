# 스택/큐는 사용 안함

def solution(arr):
    # answer 배열에 arr 첫번째 값 삽입
    answer = []    
    answer.append(arr[0])
    # arr 배열 하나씩 돌면서
    # answer 마지막 값과 같은지 판단
    for i in range(len(arr)):
        # 같으면 패스
        if arr[i] == answer[-1]:
            continue
        # 틀리면 answer에 추가
        else:
            answer.append(arr[i])
    ## return answer
    return answer