# coding: UTF-8

import sys

# main
#================================================================
str = sys.argv[1]

decimal = int(str)
print("decimal=", decimal)

binary = bin(decimal)
print("binary", binary)
for i in range(2, len(binary)):
    print(binary[i], end=" ")

print()
#================================================================
