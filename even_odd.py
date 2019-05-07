def number():
    num=int(input("enter an integer: "))
    if num%2==0:
        print("You entered an even number")
        if num%4==0:
            print("Your number is also a multiple of 4")
    else:
        print("You entere an odd number")
number()
