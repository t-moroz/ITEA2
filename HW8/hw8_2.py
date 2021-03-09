def delitel():
    while True:
        try:
            a=int(input('Enter a number, please:'))
            s=[]
            for b in range(1,(a+1)):
                if a%b==0:
                    s.append(b)

            print(s)
        except ValueError:
            print('Enter only numbers!')
    #return
delitel()