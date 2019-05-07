def devide():
    num=int(input("Enter numerator: "))
    den=int(input("Enter denomenator: "))
    try:
        (num/den)
    except:
        print("You can not devide by zero")
        devide()
    else:
        print("Division is: ",(num/den))
devide()
