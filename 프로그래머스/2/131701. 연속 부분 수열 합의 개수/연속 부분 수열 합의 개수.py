def solution(elements):
    
    circle = elements * 2
    print(circle) 
    cnt = 0
    dupl = set()
    for l in range(1,len(elements)+1):
        sum_ = 0
        for k in range( len(circle) - l):
            now = sum(circle[k:k+l])
            if now not in dupl:
                # print(l, circle[k:k+l])
                dupl.add(now)
                cnt += 1
            
    
    answer = cnt
    return answer