# Phoenix has n coins with weights 2^1,2^2,…,2^n. He knows that n is even.
# He wants to split the coins into two piles such that each pile has exactly
# n2 coins and the difference of weights between the two piles is minimized.
#  Formally, let a denote the sum of weights in the first pile,
#  and b denote the sum of weights in the second pile. Help Phoenix minimize |a−b|,
#  the absolute value of a−b.


t = int(input())
for i in range(t):
    n = int(input())
    a, b = 2**n, 0

    print(a)
    print(b)
    k = int(n//2)
    i = 1
    while i < k:
        a += (2**i)
        i += 1
    while i < n:
        b += (2**i)
        i += 1
    print(a-b)

# t = int(input())
# p = 0
# for i in range(t):
#     n = int(input())
#     l = int((n/2) + 1)
#     p = 2**l
#     print(p-2)
