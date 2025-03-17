def solution(money):
    money_1 = money[:-1]
    money_2 = money[1:]
    # print(money_1)
    # print(money_2)
    
    n = len(money)
    
    dp_1 = [0] * (n-1)
    dp_1[0] = money_1[0]
    dp_1[1] = max(money_1[0], money_1[1])
    for i in range(2, n-1):
        dp_1[i] = max(dp_1[i-1], dp_1[i-2] + money_1[i])
        # print(dp_1)
    
    # print("---------------------------------------")
    dp_2 = [0] * (n-1)
    dp_2[0] = money_2[0]
    dp_2[1] = max(money_2[0], money_2[1])
    for j in range(2, n-1):
        dp_2[j] = max(dp_2[j-1], dp_2[j-2] + money_2[j])
        # print(dp_2)
        
    answer = max(dp_1[-1], dp_2[-1])
    # answer = 0
    return answer