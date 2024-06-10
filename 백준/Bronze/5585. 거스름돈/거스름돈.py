paid = int(input())
money = [500,100,50,10,5,1]
changes = 1000-paid

cnt = 0
if changes == 0:
    print(cnt)
else:
    for m in money:
        if changes//m > 0:
            cnt += changes//m
            changes = changes%m

        if changes == 0:
            print(cnt)
            break
