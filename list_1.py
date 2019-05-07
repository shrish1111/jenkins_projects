def list1():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for i in a:
        if i<10:
            print(i)
    b =[]
    for j in a:
        if j<5:
            b.append(j)
    print(b)
    num=int(input("enter number: "))
    c =[]
    for k in a:
        if k<num:
            c.append(k)
    print(c)
list1()
