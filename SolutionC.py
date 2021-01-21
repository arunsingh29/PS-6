l = int(input())

h,b = [int(x) for x in input().split()]

L = [int(x) for x in input().split()]

A = h*b

M = sorted(L)
sumation = sum(L)
ans = 0

for i in M:
    m = 0
    maxi = 0
    for j in L:
        if i <= j:
            m += i*A
        else:
            m = 0
        if m>maxi:
            maxi = m
    if maxi>ans:
        ans = maxi

print(sumation -ans)
