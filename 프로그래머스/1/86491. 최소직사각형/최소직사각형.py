def solution(sizes):
    answer = 0
    
    width = 0
    height = 0
    
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]
        if width < i[0]:
            width = i[0]
        if height < i[1]:
            height = i[1]
            
    answer = width * height
    return answer