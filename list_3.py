def list1():
    num1=int(input("Enter lower limit: "))
    num2=int(input("Enter upper limit: "))
    a=[]
    for i in range(num1,num2+1):
        a.append(i)
    print(a)
list1()
