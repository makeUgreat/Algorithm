from collections import deque
def solution(food):
    answer = deque()
    answer.append(0)

    
    for i in range(len(food)-1,-1,-1):
        if food[i] % 2 == 1:
            cnt = food[i]-1
        else:
            cnt = food[i]
        
        
        for j in range(cnt):
            if j%2 == 0:
                answer.append(i)
            else:
                answer.appendleft(i)
    

    return     ''.join(map(str,answer))