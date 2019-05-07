def divisors():
    num=int(input("Enter number: "))
    a=[]
    for i in range(1,num):
        if num%i==0:
            a.append(i)
    print("All divisors of",num,"are",a)
divisors()
