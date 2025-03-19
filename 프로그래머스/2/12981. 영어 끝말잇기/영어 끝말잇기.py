def solution(n, words):
    
    # 초기값 설정
    # words의 첫번째 글자 첫번째 문자
    used_words = [words[0][0]]
    # 사람 번호, 차례
    num, turn = 0, 0
    index = 0
    
    for word in words:
        index += 1
        # 이미 사용했던 단어일 때
        if word in used_words:
            # 사람 번호 구하기
            num = index % n if index % n != 0 else n
            # 몇 번째 차례인지 구하기
            turn = index // n + 1 if index % n != 0 else index // n
            return [num, turn]
        elif word[0] != used_words[-1][-1]:
            num = index % n if index % n != 0 else n
            turn = index // n + 1 if index % n != 0 else index // n
            return [num, turn]
        else:
            # 끝말잇기 성공하면 used_words에 단어 추가
            used_words.append(word)
    
    # 탈락한 사람 없음
    return [0, 0]