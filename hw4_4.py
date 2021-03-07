while True:
    while True:
        try:
            d=int(input('Enter year, please:'))
            print(d)
            break
        except:
            print('Only number, please!')

    if d%4==0:
        print('This is a leap year!')
    elif d%100==0 and d%400==0:
        print('This is a leap year!')
    else:
        print("This isn't a leap year")

