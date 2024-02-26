def solution(numbers):
    answer = set()
    # numbers 정렬하고 완전탐색? 
    numbers.sort()
    n = len(numbers)
    for i in range(n-1):
        for j in range(i+1,n):
            answer.add(numbers[i]+numbers[j])
            
    return sorted(list(answer))