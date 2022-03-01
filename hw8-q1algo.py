from sympy import *
x, y, z = symbols('x, y, z')

A = Matrix([[3,0],[1,-2],[3,1]])
b = Matrix([9,7,7])
ata = A.transpose() * A
print(ata)
atb = A.transpose() * b
print(atb)
aug1 = ata.col_insert(2,atb)
print(aug1)
#print(aug1[:,:-1].rref())
x_hat = solve_linear_system(aug1, x, y)
x_hat = Matrix([x_hat[x],x_hat[y]])
print(x_hat)

b_v = A * x_hat
print(b_v)
print(b_v-b)
# A = Matrix([[56,30,50,-126],[30,30,-15,-135],[50,-15,170,90]])
# print(A_1 * Matrix([Rational(9,26),Rational(-63,13),0]))
# Matrix([-9, Rational(297,13), Rational(-36,13)]) - Matrix([-6,-24,-3])
# print(A[:,:-1].rref())
# print(solve_linear_system(A, x, y, z))