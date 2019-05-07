def gcd(x,y):
    i = min(x,y)
    gcd_list=[]
    for k in range(1,i):
        if (x%k==0 and y%k==0):
            gcd_list.append(k)
    print("gcd is",max(gcd_list))
def main():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    gcd(a,b)
main()
