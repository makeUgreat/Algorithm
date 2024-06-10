def max_moves(a,b,c):
    return max(b-a,c-b)-1

while 1:
    try:
        a,b,c = map(int,input().split())
        print( max_moves(a,b,c))
    except:
        break