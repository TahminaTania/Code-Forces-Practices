x = int(input())
for i in range(x):
    a, b, c, d, e, f = map(int, input())
    if a+b+c == d+e+f:
        print("YES")
    else:
        print("NO")
