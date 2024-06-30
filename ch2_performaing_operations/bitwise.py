#!/usr/bin/env python3.12

a = 10
b = 5

print('a =', a, '\tb =', b)

# 1010 ^ 0101 = 1111 (decimal 15)
b = a ^ b

# 1111 ^ 1010 = 0101 (decimal 5)
a = a ^ b

print('a = ', a, '\tb = ', b)

