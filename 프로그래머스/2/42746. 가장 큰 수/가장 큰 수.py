def solution(numbers):
    numbers = list(map(str, numbers))
    numlist = []
    for i in numbers:
        numlist.append((i, (i * 4)[:4]))
        
    numlist.sort(key = lambda x: x[1], reverse = True)
    
    answer = ''
    for x in numlist:
        answer += x[0]

    if answer == '' or answer[0] == "0":
        return "0"
        
    return answer