# coding: UTF-8

import sys
#Calculate order
#================================================
def gcd(x, y):
    while y != 0:
        x,y = y,x%y
    return x

def euler(n):
    if n==1: return 1
    cnt = 0
    for i in range(1, n):
        if gcd(n, i) == 1:
            cnt += 1
    return cnt

p = int(sys.argv[1])

print (euler(p))


# #Calculate primitive root
# print("primitive root(mod ", p, ")=", end="")
# for a in range(2, p):
#     if order(a, p)==p-1:
#         print(a, end="")
#         break
# print()
