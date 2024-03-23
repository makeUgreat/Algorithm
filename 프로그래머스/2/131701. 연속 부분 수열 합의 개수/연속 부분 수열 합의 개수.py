def solution(elements):
    # 누적합으로 최적화해보자
    prefixSum = [0]
    
    for e in elements:
        prefixSum.append(prefixSum[-1]+e)
        
    only = set()
    for start in range(len(elements)):
        for length in range(1,len(elements)+1):
            end = start + length - 1
            
            sum_ = prefixSum[end%len(elements)] - prefixSum[start] + (prefixSum[-1] if end >= len(elements) else 0 ) 
            only.add(sum_)
            
    
    return len(only)
    
    
    # 기존풀이
    
#     circle = elements * 2
#     cnt = 0
#     dupl = set()
#     for l in range(1,len(elements)+1):
#         sum_ = 0
#         for k in range( len(circle) - l):
#             now = sum(circle[k:k+l])
#             if now not in dupl:
#                 # print(l, circle[k:k+l])
#                 dupl.add(now)
#                 cnt += 1
            
    
#     answer = cnt
#     return answer