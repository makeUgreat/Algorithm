def solution(name, yearning, photo):
    answer = []
    score = dict()
    
    for n,y in zip(name,yearning):
        score[n] = y
        
    for p in photo:
        sum_ = 0
        for n in p:
            if n not in score:
                pass
            else:
                sum_ += score[n]
        answer.append(sum_)    
            
    return answer