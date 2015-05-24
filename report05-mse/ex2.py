# ex2.py and ex3.py
# 2015/05/24
# Haruyuki Ichino
# Report 5th of mse. Show QRp and QNRp

#conding: UTF-8

# define
# ===========================================================
p = 521
g = 3
y = 467
c1 = 510
c2 = 258

QR = []
QNR = []

def checkArray(x, array):
    for i in array:
        if (x==i): return True
# ===========================================================
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

print ("QR = ", QR)
print ("QNR = ", QNR)
