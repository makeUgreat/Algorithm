def solution(people, limit):
    sorted_people = sorted(people,reverse=True)
    boats = 0
    left = 0
    right = len(people) -1
    
    while left <= right:
        if sorted_people[left] + sorted_people[right] <= limit:
            right -= 1
        left += 1
        boats += 1
            
    return boats
