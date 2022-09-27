x = int(input())

th = tm = 0
for i in range(x):
    h, m = [int(x) for x in input().split()]
    if (h <= 24):
        tm = 60-m
        th = 23-h
        tm = (th*60)+tm
    print(tm)
