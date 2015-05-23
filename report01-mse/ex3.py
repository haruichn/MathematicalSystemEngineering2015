# ex3.py
# Haruyuki Ichino
# 2015/04/14

#coding: UTF-8
import sys
import random

def calp(p):
    return (2**0)*p[0] + (2**1)*p[1] + (2**2)*p[2] + (2**3)*p[3] + (2**4)*p[4] + (2**5)*p[5] + (2**6)*p[6] + (2**7)*p[7] + (2**8)*p[8] + (2**9)*p[9] + (2**10)*p[10] + (2**11)*p[11] + (2**12)*p[12] + (2**13)*p[13] + (2**14)*p[14] + (2**15)

#check prime number
#===================================================
def is_prime3(q,k=50):
    q = abs(q)
    #計算するまでもなく判定できるものははじく
    if q == 2: return True
    if q < 2 or q&1 == 0: return False

    #n-1=2^s*dとし（但しaは整数、dは奇数)、dを求める
    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1

    #判定をk回繰り返す
    for i in range(k):
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)
        #[0,s-1]の範囲すべてをチェック
        while t != q-1 and y != 1 and y != q-1:
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False
    return True
#================================================


str = sys.argv[1] #a15,a14,a13,...,a0

num = [] # init num
#set inpu tnum
for i in range(16):
    num.append(int(str[15-i])) #num=[a0,a1,a2,...,a15]

pd = calp(num)
p = pd + 1
while(not is_prime3(p)):
   p=p+1

print(p)

pcount = 0
for i in range(2, p):
    if is_prime3(i)==True:
        pcount = pcount + 1
        print(i)

print ('Prime count =', pcount)
