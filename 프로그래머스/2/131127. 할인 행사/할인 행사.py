def stock_check(want_stock):
    for k,v in want_stock.items():
        if v != 0:
            return True
    return False

def solution(want, number, discount):  
    # discount 배열에서 want 배열 길이 만큼 슬라이싱 윈도우해서
    # 다 있으면 해당 슬라이스 배열의 인덱스 번호를 리턴한다
    lng = len(want)
    want_stock = dict()
    # 품목별 재고 딕셔너리로 만들기
    for k,v in zip(want,number):
        want_stock[k] = v
        
        
    answer = 0
    for i in range(len(discount)-9):
        for k,v in zip(want,number):
            want_stock[k] = v
            
        now_sales = discount[i:i+10]
        
        for item in now_sales:
            if want_stock.get(item):
                want_stock[item] -= 1
        
        if stock_check(want_stock): continue
    
        answer += 1
        
    return answer