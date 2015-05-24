# ex1.py
# 2015/05/24
# Haruyuki Ichino
# Report 5th of mse. Calculate (m/p)

#conding: UTF-8

# define
# ===========================================================
p = 521
g = 3
y = 467
c1 = 510
c2 = 258

def checkArray(x, array):
    for i in array:
        if (x==i): return True

def legendre(a):
    if (checkArray(a, QR)):
        return 1
    else:
        return -1
# ===========================================================

# set QR and QNR
# ===========================================================
QR = []
QNR = []

for i in range(1, p):
    num = (i*i)%p
    if (not checkArray(num, QR)):
        QR.append(num)
for i in range(1, p):
    if (not checkArray(i, QR)):
        if (not checkArray(i, QNR)):
            QNR.append(i)

QR.sort()
QNR.sort()
# ===========================================================

# main
# ===========================================================
if (legendre(y)==1):
    print ("(m/p) = ", int(legendre(c2)))
else:
    print ("(m/p) = ", int(legendre(c2)/legendre(c1)))




# ===========================================================
