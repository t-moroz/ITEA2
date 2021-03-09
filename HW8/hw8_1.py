def acronim():
    while True:
        a=input('Input text, please:')
        b=a.upper()
        a=''.join(x[0] for x in b.split())
        print(a)
    #return a
acronim()

