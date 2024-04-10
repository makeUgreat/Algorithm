import sys
input = sys.stdin.readline

n,m = map(int,input().split())
table = dict()

for _ in range(n):
    url,pwd = input().strip().split(' ')
    table[url] = pwd

for _ in range(m):
    print(table[input().strip()])