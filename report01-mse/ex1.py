# ex1.py
# Haruyuki Ichino
# 2015/04/14

#coding: UTF-8
import sys

def calp(p):
    return (2**0)*p[0] + (2**1)*p[1] + (2**2)*p[2] + (2**3)*p[3] + (2**4)*p[4] + (2**5)*p[5] + (2**6)*p[6] + (2**7)*p[7] + (2**8)*p[8] + (2**9)*p[9] + (2**10)*p[10] + (2**11)*p[11] + (2**12)*p[12] + (2**13)*p[13] + (2**14)*p[14] + (2**15)

str = sys.argv[1] #a15,a14,a13,...,a0

num = [] # init num
#set num
for i in range(16):
    num.append(int(str[15-i])) #num=[a0,a1,a2,...,a15]

#for i in range(16):
#   print(num[i])

print(calp(num))
