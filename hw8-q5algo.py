from sympy import *
B,C,D,E,F = symbols('B,C,D,E,F')

points = [(1,3),(3,1.5),(2.5,0),(1,-1),(-0.5,-1),(-2,0),(-2.5,2),(-1.5,3.5)]
matrix_temp = []
b_temp = []
for point in points:
    matrix_temp.append([point[1]**2, point[0] * point[1], point[0], point[1],1])
    b_temp.append(point[0]**2)
    
A = Matrix(matrix_temp)
print("A: ", A)
b = Matrix(b_temp)
print("B: ", b)
#A = Matrix([[1,1,1],[1,-1,1],[-1,1,1],[-1,-1,1]])
#b = Matrix([1,-2,3,1])
ata = A.transpose() * A
print("ata: ", ata)
atb = A.transpose() * b
print("atb: ",atb)
aug1 = ata.col_insert(6,atb) # !!! THIS LINE
print("aug: ",aug1)
#print(aug1[:,:-1].rref())
x_hat = solve_linear_system(aug1, B,C,D,E,F)
x_hat = Matrix([x_hat[B],x_hat[C],x_hat[D],x_hat[E],x_hat[F]])
print("x_hat: ",x_hat)

b_v = A * x_hat
print("b_v: ",b_v)
print("b_vperp: ",b_v-b)
# A = Matrix([[56,30,50,-126],[30,30,-15,-135],[50,-15,170,90]])
# print(A_1 * Matrix([Rational(9,26),Rational(-63,13),0]))
# Matrix([-9, Rational(297,13), Rational(-36,13)]) - Matrix([-6,-24,-3])
# print(A[:,:-1].rref())
# print(solve_linear_system(A, x, y, z))