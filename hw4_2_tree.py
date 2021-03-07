
while True:
    try:
        x = int(input('Enter integer number, please:'))
        if x <= 0:
            print('Enter integer number>0')
        else:
            for a in range(1, x + 1):
                print((x-a)*' ' + a*'* ')
    except:
        print('Enter number!')