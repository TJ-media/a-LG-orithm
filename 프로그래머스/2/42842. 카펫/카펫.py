def solution(brown, yellow):
    total = brown + yellow
    div = []
    for i in range(3, total//3+1):
        if total % i == 0:
            div.append(i)
    
    print(total)
    print(div)

    answer = []
    for j in div:
        print(j - 2)
        print(total//j - 2)
        if (j - 2) * (total//j - 2) == yellow:
            answer.append(j)
            answer.append(total//j)
        else:
            continue

    return [answer[-2], answer[-1]]