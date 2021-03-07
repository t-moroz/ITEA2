while True:
    while True:
        try:
            d=int(input('Enter year, please:'))
            print(d)
            break
        except:
            print('Only number, please!')

    if d%4==0:
        print('This is a high year!')
    elif d%100==0 and d%400==0:
        print('This is a high year!')
    else:
        print('This is a usual year')
