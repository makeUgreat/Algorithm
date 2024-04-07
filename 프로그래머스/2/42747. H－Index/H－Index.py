def solution(citations):
    sorted_cite = sorted(citations)
    answer = 0
    
    for idx in range(len(citations)):
        cnt_cite = sorted_cite[idx]
        rest_cite = len(citations) - idx
        if cnt_cite >= rest_cite:
            return rest_cite
            
    
    return answer