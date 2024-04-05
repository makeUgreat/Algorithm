def solution(n, left, right):
    answer = []
    for idx in range(left,right+1):
        x = (idx%n) 
        y = (idx//n)
        answer.append(max(x+1,y+1))
    
    return answer