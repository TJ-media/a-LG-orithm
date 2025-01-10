def solution(participant, completion):
    # 해시테이블(딕셔너리 만듦)
    answer = dict()
    # participant에 있는 사람들
    # 키는 이름으로, 밸류는 인원수로 딕셔너리에 추가
    for i in participant:
        if i in answer:
            answer[i] += 1
        else:
            answer[i] = 1
            
    # completion에 있는 사람들을 돌면서
    # 딕셔너리에 있는 인원수 한명씩 줄이기
    for j in completion:
        if j in answer:
            answer[j] -= 1
            
    # 인원수 1이상인 사람 모두 출력
    for key, value in answer.items():
        if value > 0:
            return key