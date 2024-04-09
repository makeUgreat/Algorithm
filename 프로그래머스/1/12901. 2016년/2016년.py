def solution(a, b):
    days = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    
    this_month_till_days = sum(months[:a-1]) + b
    this_day = days[this_month_till_days % 7] 
    
    answer = this_day
    return answer 