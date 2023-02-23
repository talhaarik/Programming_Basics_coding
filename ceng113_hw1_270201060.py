firstEquation = list(str(input("Enter the first equation:\n")))

copy = ['0']
x1 = ['0']
y1 = ['0']

eqIndex = firstEquation.index("=")
eq1LHS = firstEquation[: eqIndex]
eq1RHS = firstEquation[eqIndex + 1:]

for i in range(len(eq1RHS)):
    if(eq1RHS[i] == '-'):
        eq1RHS[i] = '+'
    elif(eq1RHS[i] == '+'):
        eq1RHS[i] = '-'

eq1LHS.extend(eq1RHS)

copy = eq1LHS[:]

j = 0

for i in range(len(eq1LHS)):
    if(eq1LHS[i] == 'x'):
        j = i
        while True:
            if(eq1LHS[j] == '+' or eq1LHS[j] == '-'):
                x1.extend(eq1LHS[j:i])
                break
            copy[j] = '0'
            j -= 1

    elif(eq1LHS[i] == 'y'):
        j = i
        while True:
            if(eq1LHS[j] == '+' or eq1LHS[j] == '-'):
                y1.extend(eq1LHS[j:i])
                break
            copy[j] = '0'
            j -= 1

ret_x1 = eval(''.join(x1))
ret_y1 = eval(''.join(y1))
ret_copy = eval(''.join(copy))

X1 = ret_x1
Y1 = ret_y1
C1 = ret_copy

secondEquation = list(str(input("Enter the second equation:\n")))

copy2 = ['0']
x2 = ['0']
y2 = ['0']

eqIndex2 = secondEquation.index("=")
eq2LHS = secondEquation[: eqIndex2]
eq2RHS = secondEquation[eqIndex2+1 :]

for i2 in range(len(eq2RHS)):
    if(eq2RHS[i2] == '-'):
        eq2RHS[i2] = '+'
    elif(eq2RHS[i2] == '+'):
        eq2RHS[i2] = '-'

eq2LHS.extend(eq2RHS)

copy2 = eq2LHS[:]

j2 = 0

for i2 in range(len(eq2LHS)):
    if(eq2LHS[i2] == 'x'):
        j2 = i2
        while True:
            if(eq2LHS[j2] == '+' or eq2LHS[j2] == '-'):
                x2.extend(eq2LHS[j2:i2])
                break
            copy2[j2] = '0'
            j2 -= 1

    elif(eq2LHS[i2] == 'y'):
        j2 = i2
        while True:
            if(eq2LHS[j2] == '+' or eq2LHS[j2] == '-'):
                y2.extend(eq2LHS[j2:i2])
                break
            copy2[j2] = '0'
            j2 -= 1

ret_x2 = eval(''.join(x2))
ret_y2 = eval(''.join(y2))
ret_copy2 = eval(''.join(copy2))

X2 = ret_x2
Y2 = ret_y2
C2 = ret_copy2

X1 *= -X2
Y1 *= -X2
C1 *= -X2

X2 *= ret_x1
Y2 *= ret_x1
C2 *= ret_x1

constant = 0
if (ret_x2 > ret_x1):
    constant = -(ret_x2/ret_x1)

    x_coefficient = (constant * ret_x1) + ret_x2   # Adding the x values with the x values, a new x coefficient is obtained.
    y_coefficient = (constant * ret_y1) + ret_y2   # Adding the y values with the y values, a new y coefficient is obtained.

    result1 = -(constant * ret_copy)
    result2 = -(ret_copy2)

    result = result1 + result2

    solutionForY= (result/ y_coefficient)   # We have the equation y = constant. It is done to get y.
    solutionForX = ((-ret_y1*solutionForY) - ret_copy) / ret_x1
else:
    constant = -(ret_x1 / ret_x2)

    x_coefficient = (constant * ret_x2) + ret_x1
    y_coefficient = (constant * ret_y2) + ret_y1

    result1 = -(constant * ret_copy2)
    result2 = -(ret_copy)

    result = result1 + result2

    solutionForY = (result / y_coefficient)
    solutionForX = ((-ret_y2 * solutionForY) - ret_copy2) / ret_x2
if ret_y1 < 0:
    simplified_1= f"{ret_x1}x{ret_y1}y={-ret_copy}"
else:
    simplified_1= f"{ret_x1}x+{ret_y1}y={-ret_copy}"

if ret_y2 <0 :
    simplified_2=f"{ret_x2}x{ret_y2}y={-ret_copy2}"
else:
    simplified_2=f"{ret_x2}x+{ret_y2}y={-ret_copy2}"

print(f"Equations in the simplified form:")
print(f"{simplified_1}\n{simplified_2}")
print(f"Solution:\nx={int(solutionForX)}\ny={int(solutionForY)}")
