for x in range(int(input())):
    w, h, n = [int(x) for x in input().split()]
    cnt = 1
    while w % 2 == 0:
        cnt *= 2
        w //= 2

    while h % 2 == 0:
        cnt *= 2
        h //= 2

    print("YES") if cnt >= n else print("NO")
