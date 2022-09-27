

for i in range(int(input())):
    a = list(map(int, (input().split())))

    if min(max(a[0], a[1]), max(a[2], a[3])) > max(min(a[0], a[1]), min(a[2], a[3])):
        print("YES")
    else:
        print("No")
