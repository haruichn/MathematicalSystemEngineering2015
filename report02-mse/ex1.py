# ex1.py on report02
# Haruyuki Ichino
# 2015/04/23

# coding: UTF-8
import sys
import random

# define function
#================================================================
def calp(p):
    return (2**0)*p[0] + (2**1)*p[1] + (2**2)*p[2] + (2**3)*p[3] + (2**4)*p[4] + (2**5)*p[5] + (2**6)*p[6] + (2**7)*p[7] + (2**8)*p[8] + (2**9)*p[9] + (2**10)*p[10] + (2**11)*p[11] + (2**12)*p[12] + (2**13)*p[13] + (2**14)*p[14] + (2**15)

#check prime number
def is_prime3(q,k=50):
    q = abs(q)

    if q == 2: return True
    if q < 2 or q&1 == 0: return False

    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1

    for i in range(k):
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)

        while t != q-1 and y != 1 and y != q-1:
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False
    return True

#Calculate order
def order(m, p):
    count = 1
    res = m
    while res != 1:
        res = (res*m)%p
        count = count+1

    return count
#================================================================


# main
#================================================================
str = sys.argv[1] #a15,a14,a13,...,a0

num = [] # init num
#set input num
for i in range(16):
    num.append(int(str[15-i])) #num=[a0,a1,a2,...,a15]

pd = calp(num)

p = pd + 1
while(not is_prime3(p)):
   p=p+1

print("p =", p)

pcount = 0
plist =[]
for i in range(2, p):
    if is_prime3(i)==True:
        pcount = pcount + 1
        plist.append(i)
        #print(i)
#print ('Prime count =', pcount)

#factorization in prime numbers
pfd = p - 1
#print("p-1 = ", p-1)

#Calculate primitive root
print("primitive root(mod ", p, ") = ", end="")
for a in range(2, p):
    if order(a, p)==p-1:
        print(a, "...")
        break
#================================================================
