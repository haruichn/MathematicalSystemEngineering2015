# test code
# Haruyuki Ichino
# 2015/04/24

# coding: UTF-8
import sys

# func
#================================================================
def fpower(a,b):
    binary = bin(b) #trans10to2
    ans = a
    for i in range(3, len(binary)):
        if binary[i] == 1:
            ans = ans * ans * a
        else:
            ans = ans * ans

    return ans
#================================================================

# main
#================================================================
g = int(sys.argv[1])
x = int(sys.argv[2])
print(g,"^(",x,") = ", end="")
print(fpower(g,x))
#================================================================
