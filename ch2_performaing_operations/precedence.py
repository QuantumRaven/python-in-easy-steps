#!/usr/bin/env python3.12

a = 2
b = 4
c = 8

print('\nDefault Order:\t', a, '*', c, '+', b, '=', a * c + b)
print('\nForced Order:\t', a, '* (', c, '+', b, ') =', a * (c + b))

print('\nDefault Order:\t', c, '//' b, '-', a, '=', c // b - a)
print('Forced Order:\t', c, '// (', b, '-', a, ') =', c // (b - a))
