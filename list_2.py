def list1():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c=[]
    d=[]
    for i in a:
        for j in b:
            if i==j:
                c.append(i)
    d=list(set(c))
    print("Common elements in both lists are: ",d)
list1()
                