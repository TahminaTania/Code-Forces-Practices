x = int(input())
t = c = 1

while x > 0:
    c += 1
    t += c
    x -= t
print(c-1)
