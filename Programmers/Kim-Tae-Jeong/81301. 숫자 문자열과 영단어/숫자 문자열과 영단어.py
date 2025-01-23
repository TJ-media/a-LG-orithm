def solution(s):
    answer = ''
    while s:
        # zero
        if s[0] == 'z':
            answer += '0'
            s = s[4:] # "zero----"
        # one
        elif s[0] == 'o':
            answer += '1'
            s = s[3:] # "one----"
        # two
        elif s[0] == 't' and s[1] == 'w':
            answer += '2'
            s = s[3:] # "two----"    
        # three
        elif s[0] == 't' and s[1] == 'h':
            answer += '3'
            s = s[5:] # "three----"
        # four
        elif s[0] == 'f' and s[1] == 'o':
            answer += '4'
            s = s[4:] # "four----"
        # five
        elif s[0] == 'f' and s[1] == 'i':
            answer += '5'
            s = s[4:] # "five----"    
        # six
        elif s[0] == 's' and s[1] == 'i':
            answer += '6'
            s = s[3:] # "six----"
        # seven
        elif s[0] == 's' and s[1] == 'e':
            answer += '7'
            s = s[5:] # "seven----"
        # eight
        elif s[0] == 'e':
            answer += '8'
            s = s[5:] # "eight----" 
        # nine
        elif s[0] == 'n':
            answer += '9'
            s = s[4:] # "nine----" 
        # 숫자
        else:
            answer += s[0]
            s = s[1:] # "X----"
        
    answer = int(answer)
    return answer