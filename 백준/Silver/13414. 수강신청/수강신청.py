capa, needs = map(int,input().split())
q = dict()

for i in range(needs):
    stu_num = input()
    q[stu_num] = i

sorted_q = sorted(q.items(), key=lambda item: item[1])

for stu,v in sorted_q[:capa]:
    print(stu)

