def solution(s):
    answer = ""
    my_dict = {
        "zero" : 0,
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }
    
    tmp = ""
    for c in s:
        if c.isalpha():
            tmp += c
        else:
            answer += c
        
        IsSentence = my_dict.get(tmp,None)
        if IsSentence is not None:
            answer += str(IsSentence)
            tmp = ""
    
    return int(answer)