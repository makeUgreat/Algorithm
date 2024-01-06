def solution(s, n):
    answer = []
    stringToAsci = list(map(ord,s))
    for ch in stringToAsci:
        tmp = 0
        # 공백 제외
        if ch == 32:
            answer.append(' ')
            continue
        # if 대문자
        if ch >= 65 and ch <= 90:
            tmp = ((ch + n - 65) % 26) + 65 
        # if 소문자
        if ch >= 97 and ch <= 122:
            tmp = ((ch + n - 97) % 26) + 97
            
            
        answer.append(chr(tmp))
        
    answer = ''.join(answer)
        
    return answer



# 65~90 'AZ' / 97 ~ 122 'az' / ' ' = 32