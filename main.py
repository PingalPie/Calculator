import numpy as np
# Module to find Square root, Cube root

loop = 1
# int for loop

while int(loop) == int(loop):
    opr = input('''What operation you want to do (+,-,/,*,##,^,^^,//,///) [// Means square root, ^ means square,
    /// means cube root, ^^ means cube, ## means average] -  ''')
    # Asking what operation you want to do 
    
    if opr == '+':
        add = float(input('Enter first number - '))
        add2 = float(input('Enter second number - '))
        res = add + add2
        print(add, '+', add2, '=', res)
    # For addition
    
    elif opr == '-':
        sub = float(input('Enter first number - '))
        sub2 = float(input('Enter second number - '))
        re = sub - sub2
        print(sub, '-', sub2, '=', re)
    # For subtraction
    
    elif opr == '*':
        mul = float(input('Enter first number - '))
        mul2 = float(input('Enter second number - '))
        r = mul * mul2
        print(mul, '*', mul2, '=', r)
    # For multiplication
    
    elif opr == '/':
        div = float(input('Enter first number - '))
        div2 = float(input('Enter second number - '))
        dip = div/div2
        print(div, '/', div2, '=', dip)
    # For division
    
    elif opr == '^':
        sq = float(input('For what number you want to find square - '))
        s = sq**2
        print(sq, '*', sq, '=', s)
    # For square
    
    elif opr == '//':
        sqr = float(input('For what number you want to find square root - '))
        rrr = np.sqrt(sqr)
        print('Root of ', sqr, 'is', rrr)
    # For square root
    
    elif opr == '^^':
        cbe = int(input('For what number you want to find cube - '))
        cc = cbe**3
        print('cube of ', cbe, 'is', cc)
    # For cube
    elif opr == '///':
        cube_num = float(input('For what number you want to find cube root - '))
        cube_pow = np.cbrt(float(cube_num))
        print('Root of ', cube_num, 'is', cube_pow)
    # For cube root
    elif opr == '##':
        num1 = float(input('Enter the first number - '))
        num2 = float(input('Enter the second  number - '))
        avg = (num1+num2)/2
        print('Average of both numbers is :- ', avg)
    # For average
