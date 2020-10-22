import math

print('A * x^2 + B * x + C = 0\nInsert coefficients for the equation:')
a = float(input('A = '))
b = float(input('B = '))
c = float(input('C = '))

D = b ** 2 - 4 * a * c
print('Discriminant D = ', D)

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print('X1 = ', x1, '\nX2 = ', x2)
elif D == 0:
    x = -b / (2 * a)
    print('X = ', x)
else:
    print('There is no solutions')
