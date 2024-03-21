me = input()
parts = me.split('-')
sum_ = sum(map(int, parts[0].split('+')))

for part in parts[1:]:
    sum_ -= sum(map(int,part.split('+')))

print(sum_)