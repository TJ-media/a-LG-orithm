def solution(nums):
    # 중복 없는 set 형태로 바꿈
    nums_set = set(nums)
    
    # (포켓몬 종류 수)와 (포켓몬 전체 수 // 2)를 비교
    if len(nums_set) < len(nums) // 2:
        answer = len(nums_set)
    else:
        answer = len(nums) // 2
    
    return answer