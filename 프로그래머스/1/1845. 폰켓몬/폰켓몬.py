def solution(nums):
    distinct = set(nums)
    if len(nums)//2 >= len(distinct):
        answer = len(distinct)
    else:
        answer = len(nums)//2
    return answer