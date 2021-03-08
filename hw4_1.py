while True:
    while True:
            try:
                number1=int(input('Input first number:'))
                break
            except: TypeError
            print('Enter only number!')
            continue

    while True:
            operation=input('Input operator:')
            if operation not in ('+','-', '*', '/', '**', '***'):
                print('Enter correct operator')
                continue
            else:
                break

    while True:
        try:
            number2=int(input('Input second number:'))
            break
        except:TypeError
        print('Enter only number!')
        continue


    if operation=='+':
        b=number1+number2
        print(b)
    elif operation=='-':
        b = number1 -number2
        print(b)
    elif operation=='*':
        b=number1*number2
        print(b)
    elif operation=='**':
        b=number1**number2
        print(b)
    elif operation=='***' and number2!=0:
        b=number1**(1/number2)
        print(b)
    elif operation=='***' and number2==0:
        print('Divide by zero')
    elif operation=='/' and number2!=0:
        b=number1/number2
        print(b)
    elif operation=='/' and number2==0:
        print('Divide by zero')
