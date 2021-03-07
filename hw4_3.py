while True:
    while True:
        try:
            n=int(input('Enter number:'))
            break
        except:
            print("Enter only integer number!")

    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    print(a)
    i = 2
    for i in range(2, n):
        for c in range(2, n):
            j = c * i
            if j <= n:
                a[j] = 0

    a = set(a)
    a.remove(0)
    print(a)
