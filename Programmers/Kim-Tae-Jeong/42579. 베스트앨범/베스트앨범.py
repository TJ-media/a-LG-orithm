def solution(genres, plays):
    
    answer = []
    
    # 딕셔너리에 담기
    dic = {}
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = []
            dic[genres[i]].append([plays[i], i])
        else: 
            dic[genres[i]].append([plays[i], i])
    
    # print(dic)
    
    # 장르별 재생 횟수 합 구하기
    play_sum = []
    for j in dic:
        genre_sum = 0
        for k in range(len(dic[j])):
            genre_sum += dic[j][k][0]
        play_sum.append([j, genre_sum])
    
    # print(play_sum)
    
    # 재생횟수 많은 장르 순으로 정렬
    play_sum.sort(key = lambda x:x[1], reverse=True)
    # dic안에서도 재생횟수 많은 노래 순으로 정렬
    for m in dic:
        dic[m].sort(key = lambda x:x[0], reverse=True)
    
    # print(play_sum)
    
    # 재생횟수 많은 장르순 -> 장르 별 2개씩 출력하기 
    for genre in play_sum:
        # 해당 장르의 노래 리스트
        songs = dic[genre[0]]
        # 첫 번째 노래 추가
        answer.append(songs[0][1])
        # 두 번째 노래가 있다면 추가
        if len(songs) > 1:
            answer.append(songs[1][1])
        
    return answer