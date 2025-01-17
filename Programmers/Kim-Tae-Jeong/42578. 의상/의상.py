def solution(clothes):
    kony = {}
    for i in range(len(clothes)): 
        if clothes[i][1] not in kony.keys():
            kony[clothes[i][1]] = 1
        else:       
            kony[clothes[i][1]] += 1

    answer = 1
    for j in kony.values():
        answer *= j + 1
        
    answer -= 1
    
    return answer